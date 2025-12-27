# core/scoring.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from .analysis import AnalysisFlags


@dataclass(frozen=True)
class ScoreResult:
    decision_fragility: int
    reflection_depth: int
    signals: Dict[str, int]


def score_reflection(
    *,
    flags: AnalysisFlags,
    answer_text: str,
    is_high_stakes: bool
) -> ScoreResult:
    """
    Scores are INTERNAL only.
    No advice, no user-facing output.
    """

    fragility = 0
    depth = 0
    signals: Dict[str, int] = {}

    text = (answer_text or "").lower()

    # --- Fragility signals ---
    if is_high_stakes:
        fragility += 2
        signals["high_stakes"] = 2

    if any(k in text for k in ("rent", "housing", "house", "evicted", "kicked out")):
        fragility += 3
        signals["housing_risk"] = 3

    if any(k in text for k in ("quit", "quitting", "income", "job", "salary")):
        fragility += 2
        signals["income_risk"] = 2

    if flags.deflection:
        fragility += 1
        signals["deflection"] = 1

    if flags.irritated:
        fragility += 1
        signals["irritation"] = 1

    if flags.emotional:
        fragility += 1
        signals["emotional"] = 1

    if any(k in text for k in ("can't undo", "cant undo", "no way back", "irreversible")):
        fragility += 2
        signals["irreversible"] = 2

    # --- Reflection depth signals ---
    if flags.low_specificity:
        depth -= 2
        signals["low_specificity"] = -2

    if flags.deflection:
        depth -= 1
        signals["deflection_depth_penalty"] = -1

    if flags.overconfidence:
        depth -= 1
        signals["overconfidence"] = -1

    # Concrete detail bonuses
    if any(ch.isdigit() for ch in text):
        depth += 2
        signals["numbers_present"] = 2

    if any(t in text for t in ("week", "month", "year", "months", "weeks")):
        depth += 1
        signals["time_horizon"] = 1

    if any(k in text for k in ("rent", "money", "time", "energy", "focus")):
        depth += 1
        signals["constraint_named"] = 1

    return ScoreResult(
        decision_fragility=fragility,
        reflection_depth=depth,
        signals=signals,
    )

