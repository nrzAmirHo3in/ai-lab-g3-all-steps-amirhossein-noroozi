"""Experiment harness: run each policy many times and report mean +/- std.

This is the piece the digit-recognition project reuses in steps 4 and 6: swap
`score` for `accuracy` and `VacuumEnv` for the dataset split, the loop stays.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import Any

import numpy as np
import pandas as pd

from .agents import Agent
from .environment import EnvConfig, VacuumEnv

METRICS = ("score", "net_score", "energy", "steps_to_clean", "idle_steps", "clean_ratio")


def run_once(agent_cls: type[Agent], cfg: EnvConfig, seed: int) -> dict[str, Any]:
    """One episode: fresh environment and fresh agent memory for the given seed."""
    env = VacuumEnv(cfg)
    agent = agent_cls(rng=np.random.default_rng(seed))
    agent.reset(cfg.n_rooms)

    obs = env.reset(seed=seed)
    steps_to_clean: int | None = None
    idle_steps = 0

    while not env.done:
        action = agent.act(obs)
        obs, _, _ = env.step(action)
        idle_steps += action == "NoOp"
        if steps_to_clean is None and env.clean_rooms == cfg.n_rooms:
            steps_to_clean = env.steps_taken

    return {
        "agent": agent.name,
        "seed": seed,
        "score": env.score,
        "energy": env.energy,
        "steps_to_clean": steps_to_clean if steps_to_clean is not None else np.nan,
        "idle_steps": idle_steps,
        "clean_ratio": env.clean_rooms / cfg.n_rooms,
    }


def evaluate(
    agent_classes: Sequence[type[Agent]],
    cfg: EnvConfig | None = None,
    runs: int = 100,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return (per-run rows, per-agent summary with mean/std/sem)."""
    cfg = cfg or EnvConfig()
    rows = [run_once(agent_cls, cfg, seed) for agent_cls in agent_classes for seed in range(runs)]
    df = pd.DataFrame(rows)
    df["net_score"] = df["score"] - df["energy"]
    summary = (
        df.groupby("agent")[list(METRICS)]
        .agg(["mean", "std"])
        .round(2)
    )
    sem = df.groupby("agent")["score"].sem().round(2)
    return df, summary.assign(score_sem=sem)


def bar_chart(summary: pd.DataFrame, metric: str = "score", ax=None):
    """Average `metric` per agent with std error bars."""
    import matplotlib.pyplot as plt

    ax = ax or plt.gca()
    means = summary[metric]["mean"]
    errs = summary[metric]["std"].fillna(0)
    ax.bar(means.index, means.values, yerr=errs.values, capsize=5, color="#4f46e5")
    ax.set_ylabel(metric.replace("_", " "))
    ax.set_title(f"Average {metric} over the runs")
    ax.tick_params(axis="x", rotation=0)
    return ax


def scenario_table(cfg: EnvConfig, agents: Iterable[type[Agent]]) -> str:
    lines = [f"rooms={cfg.n_rooms} steps={cfg.steps} dirty_prob={cfg.dirty_prob} seed=0..runs-1"]
    for agent in agents:
        lines.append(f"  - {agent.name}")
    return "\n".join(lines)
