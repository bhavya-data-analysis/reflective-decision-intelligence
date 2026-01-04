# core/intervention_stats.py
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Tuple


StateKey = Tuple[str, str, str, bool]  # (clarity, dominant_failure, phase, high_stakes)


class InterventionStats:
    """
    Lightweight learning memory for Level 5.
    Stores effectiveness of (state_key, intervention_id) pairs.
    """

    def __init__(self, path: str | None = None):
        if path is None:
            self.path = Path(__file__).parent / "intervention_stats.json"
        else:
            self.path = Path(path)

        self.stats: Dict[str, Dict] = {}
        self._load()

    # ---------- public API ----------

    def record(
        self,
        state_key: StateKey,
        intervention_id: str,
        reward: float,
        effect: str,
    ) -> None:
        sk = self._key(state_key)

        bucket = self.stats.setdefault(sk, {})
        entry = bucket.setdefault(
            intervention_id,
            {"n": 0, "avg_reward": 0.0, "harm": 0},
        )

        # incremental mean
        entry["n"] += 1
        entry["avg_reward"] += (reward - entry["avg_reward"]) / entry["n"]

        if effect == "hurt":
            entry["harm"] += 1

        self._save()

    def get(self, state_key: StateKey) -> Dict[str, Dict]:
        return self.stats.get(self._key(state_key), {})

    # ---------- internals ----------

    def _key(self, state_key: StateKey) -> str:
        return "|".join(map(str, state_key))

    def _load(self) -> None:
        if self.path.exists():
            self.stats = json.loads(self.path.read_text())

    def _save(self) -> None:
        self.path.write_text(json.dumps(self.stats, indent=2))
