"""Environment rules for the 4-room vacuum problem (refactored class code).

The class version mixed environment rules, agent policy and scoring inside one
function. Here the environment owns the state transitions only.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

ACTIONS = ("Left", "Right", "Suck", "NoOp")
MOVE_ACTIONS = ("Left", "Right")


@dataclass(frozen=True)
class EnvConfig:
    """All knobs of one scenario, so experiments are reproducible from one object."""

    n_rooms: int = 4
    steps: int = 50
    dirty_prob: float = 0.5
    seed: int = 0
    # development challenges from the slides
    redirty_prob: float = 0.0   # each step, a clean room gets dirty again with this probability
    move_cost: float = 0.0      # energy spent by Left/Right
    suck_cost: float = 0.0      # energy spent by Suck
    sensor_noise: float = 0.0   # probability the agent perceives the wrong dirt state

    @property
    def max_score(self) -> int:
        return self.n_rooms * self.steps


@dataclass(frozen=True)
class Observation:
    position: int
    dirty: bool
    all_known: bool = False


class VacuumEnv:
    """Linear row of rooms. The agent only perceives the room it stands in."""

    def __init__(self, config: EnvConfig | None = None) -> None:
        self.cfg = config or EnvConfig()
        self.rng: np.random.Generator = np.random.default_rng(self.cfg.seed)
        self.dirt = np.zeros(self.cfg.n_rooms, dtype=bool)
        self.position = 0
        self.score = 0
        self.energy = 0.0
        self.steps_taken = 0
        self.done = False

    def reset(self, seed: int | None = None) -> Observation:
        self.rng = np.random.default_rng(self.cfg.seed if seed is None else seed)
        self.dirt = self.rng.random(self.cfg.n_rooms) < self.cfg.dirty_prob
        self.position = 0
        self.score = 0
        self.energy = 0.0
        self.steps_taken = 0
        self.done = False
        return self.observe()

    def observe(self) -> Observation:
        dirty = bool(self.dirt[self.position])
        if self.cfg.sensor_noise and self.rng.random() < self.cfg.sensor_noise:
            dirty = not dirty
        return Observation(position=self.position, dirty=dirty)

    @property
    def clean_rooms(self) -> int:
        return int((~self.dirt).sum())

    def step(self, action: str) -> tuple[Observation, float, bool]:
        if action not in ACTIONS:
            raise ValueError(f"unknown action {action!r}; expected one of {ACTIONS}")
        if self.done:
            raise RuntimeError("environment is done; call reset() first")

        self._apply(action)
        self._advance_world()

        self.energy += self._step_cost(action)
        self.score += self.clean_rooms
        self.steps_taken += 1
        self.done = self.steps_taken >= self.cfg.steps
        reward = self.clean_rooms - self._step_cost(action)
        return self.observe(), reward, self.done

    def _apply(self, action: str) -> None:
        if action == "Suck":
            self.dirt[self.position] = False
        elif action == "Right":
            # bumping into the wall wastes the step but keeps the comparison fair
            self.position = min(self.position + 1, self.cfg.n_rooms - 1)
        elif action == "Left":
            self.position = max(self.position - 1, 0)

    def _advance_world(self) -> None:
        if self.cfg.redirty_prob:
            redirty = ~self.dirt & (self.rng.random(self.cfg.n_rooms) < self.cfg.redirty_prob)
            self.dirt = self.dirt | redirty

    def _step_cost(self, action: str) -> float:
        if action in MOVE_ACTIONS:
            return self.cfg.move_cost
        if action == "Suck":
            return self.cfg.suck_cost
        return 0.0
