# core/analysis.py
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class AnalysisFlags:
    deflection: bool
    overconfidence: bool
    low_specificity: bool
    emotional: bool
    irritated: bool
    matched_signals: List[str]


DEFLECTION_PHRASES: Tuple[str, ...] = (
    "doesn't matter",
    "doesnt matter",
    "not in my dictionary",
    "whatever",
    "idk",
    "i don't know",
    "dont know",
    "no idea",
    "can't explain",
    "cant explain",
    "not sure",
)

OVERCONFIDENCE_PHRASES: Tuple[str, ...] = (
    "can't fail",
    "cant fail",
    "won't fail",
    "wont fail",
    "100% sure",
    "100 percent sure",
    "no problem",
    "i don't worry",
    "i dont worry",
    "guaranteed",
    "for sure",
    "easy",
)

EMOTIONAL_WORDS: Tuple[str, ...] = (
    "anxious", "panic", "depressed", "stressed", "overwhelmed",
    "mentally", "tired", "burnt", "burned", "angry", "sad",
    "fucked", "screwed",
)

IRRITATION_PHRASES: Tuple[str, ...] = (
    "i just told you",
    "i already told you",
    "i told you",
    "man",
    "bro",
    "come on",
)

VAGUE_TOKENS: Tuple[str, ...] = (
    "stuff", "things", "something", "somehow", "whatever",
    "better", "fine", "ok", "okay", "good", "bad",
)

MIN_LEN_FOR_SPECIFICITY = 18


def _normalize(s: str) -> str:
    return (s or "").strip().lower()


def detect_flags(answer: str) -> AnalysisFlags:
    text = _normalize(answer)
    matched: List[str] = []

    deflection = any(p in text for p in DEFLECTION_PHRASES)
    if deflection:
        matched.append("deflection")

    overconfidence = any(p in text for p in OVERCONFIDENCE_PHRASES)
    if overconfidence:
        matched.append("overconfidence")

    emotional = any(w in text for w in EMOTIONAL_WORDS)
    if emotional:
        matched.append("emotional")

    irritated = any(p in text for p in IRRITATION_PHRASES)
    if irritated:
        matched.append("irritation")

    low_specificity = False
    if len(text) < MIN_LEN_FOR_SPECIFICITY:
        low_specificity = True
        matched.append("too_short")

    vague_hits = sum(1 for v in VAGUE_TOKENS if v in text)
    if vague_hits >= 2:
        low_specificity = True
        matched.append("vague_tokens")

    has_number = any(ch.isdigit() for ch in text)
    has_time_hint = any(t in text for t in ("week", "month", "year", "days", "hours"))
    if not has_number and not has_time_hint and len(text) < 40:
        low_specificity = True
        matched.append("no_time_or_numbers")

    return AnalysisFlags(
        deflection=deflection,
        overconfidence=overconfidence,
        low_specificity=low_specificity,
        emotional=emotional,
        irritated=irritated,
        matched_signals=matched,
    )
