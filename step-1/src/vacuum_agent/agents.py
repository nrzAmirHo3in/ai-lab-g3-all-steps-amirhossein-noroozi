"""Agent policies: the only part that differs between the three class agents is `act`.

Each agent sees an `Observation` (current room + dirt state of that room) and a
`rng` for reproducible randomness. Nothing here knows the scoring rules.
"""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np

from .environment import Observation


class Agent:
    """A policy maps a percept to an action."""

    name = "base"

    def __init__(self, rng: np.random.Generator | None = None) -> None:
        self.rng = rng or np.random.default_rng()

    def reset(self, n_rooms: int) -> None:
        pass

    def act(self, obs: Observation) -> str:  # pragma: no cover - interface
        raise NotImplementedError


class RandomAgent(Agent):
    """Ignores the percept entirely: Left / Right / Suck with equal probability."""

    name = "random"

    def act(self, obs: Observation) -> str:
        return str(self.rng.choice(["Left", "Right", "Suck"]))


class ReflexAgent(Agent):
    """Condition-action rule on the current room only, no memory."""

    name = "reflex"

    def act(self, obs: Observation) -> str:
        if obs.dirty:
            return "Suck"
        return str(self.rng.choice(["Left", "Right"]))


class ModelAgent(Agent):
    """Keeps a model of the row: sweeps it and stops when every room is known clean."""

    name = "model-based"

    def reset(self, n_rooms: int) -> None:
        self.n_rooms = n_rooms
        self.known_clean = np.zeros(n_rooms, dtype=bool)
        self.direction = 1
        self.tick = 0
        self._last_seen = np.full(n_rooms, -1, dtype=int)

    def _perceive(self, obs: Observation) -> None:
        self.tick += 1
        self.known_clean[obs.position] = not obs.dirty
        self._last_seen[obs.position] = self.tick

    def act(self, obs: Observation) -> str:
        self._perceive(obs)
        if obs.dirty:
            return "Suck"
        if self.known_clean.all():
            return "NoOp"
        if obs.position == self.n_rooms - 1:
            self.direction = -1
        if obs.position == 0:
            self.direction = 1
        return "Right" if self.direction == 1 else "Left"


class GoalAgent(ModelAgent):
    """Improvement over the class model agent: instead of blind back-and-forth
    sweeping, walk toward the nearest room that is dirty or still unknown."""

    name = "goal-based"
    patrol = False  # if False, behaves like the class agent and stops when all rooms look clean

    def act(self, obs: Observation) -> str:
        self._perceive(obs)
        if obs.dirty:
            return "Suck"

        targets = [i for i in range(self.n_rooms) if not self.known_clean[i]]
        if targets:
            target = min(targets, key=lambda i: abs(i - obs.position))
            return "Right" if target > obs.position else "Left"

        if not self.patrol:
            return "NoOp"
        # the world can get dirty again, so stale knowledge is not proof of a clean room:
        # re-check the room whose evidence is oldest instead of idling forever
        stale = int(np.argmin(self._last_seen))
        return "Right" if stale > obs.position else "Left"


class PatrolAgent(GoalAgent):
    name = "goal-based + patrol"
    patrol = True


AGENTS: Sequence[type[Agent]] = (RandomAgent, ReflexAgent, ModelAgent, GoalAgent, PatrolAgent)
