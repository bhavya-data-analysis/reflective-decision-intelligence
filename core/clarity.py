# core/clarity.py
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List


class DecisionClarityLevel(str, Enum):
    NONE = "none"
    EMERGING = "emerging"
    DEFINED = "defined"
    COMMITTED = "committed"


@dataclass(frozen=True)
class ClarityResult:
    level: DecisionClarityLevel
    signals: List[str]


EXPLICIT_DECISION_PHRASES = (
    "i want to",
    "i plan to",
    "i'm going to",
    "im going to",
    "i will",
    "i decided to",
)

IMPLICIT_CHANGE_PHRASES = (
    "thinking about",
    "considering",
    "maybe",
    "might",
    "not sure",
    "i guess",
    "probably",
)

COMMITMENT_PHRASES = (
    "i have decided",
    "i already quit",
    "i already moved",
    "i already did",
)


def detect_decision_clarity(text: str) -> ClarityResult:
    """
    Detects how clearly a decision is articulated.
    No judgment, no advice.
    """

    t = (text or "").strip().lower()
    signals: List[str] = []

    if not t or len(t) < 5:
        return ClarityResult(DecisionClarityLevel.NONE, ["empty_or_too_short"])

    # Committed (strongest)
    if any(p in t for p in COMMITMENT_PHRASES):
        signals.append("commitment_phrase")
        return ClarityResult(DecisionClarityLevel.COMMITTED, signals)

    # Explicit decision
    if any(p in t for p in EXPLICIT_DECISION_PHRASES):
        signals.append("explicit_decision_phrase")
        return ClarityResult(DecisionClarityLevel.DEFINED, signals)

    # Emerging / implicit
    if any(p in t for p in IMPLICIT_CHANGE_PHRASES):
        signals.append("implicit_change_phrase")
        return ClarityResult(DecisionClarityLevel.EMERGING, signals)

    # Emotional or vague statements fall here
    return ClarityResult(DecisionClarityLevel.NONE, ["no_decision_detected"])
