"""CLI: run the three class agents plus the improved one, save the tables and charts.

    PYTHONPATH=src python -m vacuum_agent.experiment --runs 100
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from .agents import AGENTS
from .environment import EnvConfig
from .evaluate import bar_chart, evaluate

RESULTS = Path(__file__).resolve().parents[2] / "results"

BASE = EnvConfig()
CHALLENGE = EnvConfig(redirty_prob=0.05, move_cost=1.0, suck_cost=3.0, sensor_noise=0.1)


def main(runs: int = 100) -> None:
    RESULTS.mkdir(exist_ok=True)
    for label, cfg in {"base": BASE, "challenge": CHALLENGE}.items():
        df, summary = evaluate(AGENTS, cfg, runs=runs)
        df.to_csv(RESULTS / f"runs_{label}.csv", index=False)
        print(f"\n=== {label}: rooms={cfg.n_rooms} steps={cfg.steps} "
              f"redirty={cfg.redirty_prob} noise={cfg.sensor_noise} ===")
        print(summary.to_string())

        fig, axes = plt.subplots(1, 2, figsize=(11, 4))
        bar_chart(summary, "score", ax=axes[0])
        bar_chart(summary, "steps_to_clean", ax=axes[1])
        fig.suptitle(f"{cfg.n_rooms} rooms, {cfg.steps} steps, {runs} runs — scenario: {label}")
        fig.tight_layout()
        fig.savefig(RESULTS / f"vacuum_{label}.png", dpi=150)
        plt.close(fig)
        print(f"saved -> {RESULTS / f'vacuum_{label}.png'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs", type=int, default=100, help="episodes per agent")
    main(**vars(parser.parse_args()))
