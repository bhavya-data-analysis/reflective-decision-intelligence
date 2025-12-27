# core/triggers.py
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class TriggerResult:
    is_high_stakes: bool
    reasons: List[str]


# Start simple: keyword + category heuristics (rules-first, local-first)
HIGH_STAKES_KEYWORDS: Tuple[str, ...] = (
    # Career / income
    "quit", "quitting", "resign", "resignation",
    "leave my job", "leave job",
    "drop out", "dropout",
    "fire", "fired", "layoff", "laid off",

    # Location / immigration
    "leave country", "leaving country",
    "move abroad", "moving abroad",
    "go back to my country", "return to my country",
    "immigrate", "immigration",
    "emigrate",
    "visa",

    # Relationships
    "break up", "divorce",
    "marry", "marriage",

    # Assets / finance
    "sell my house", "buy a house",
    "take a loan", "loan", "debt",

    # Health
    "surgery", "operation",
)

# Lightweight “domains” to grow later
DOMAIN_HINTS: Tuple[str, ...] = (
    # Work / career
    "job", "career", "company", "manager", "work",

    # Relationships
    "relationship", "marriage", "family",

    # Money
    "money", "finance", "loan", "rent",

    # Health
    "health", "doctor",

    # Location / immigration
    "move", "relocate",
    "country", "abroad", "visa", "immigration",
)


def detect_high_stakes(decision_text: str) -> TriggerResult:
    text = (decision_text or "").strip().lower()
    reasons: List[str] = []

    # Strong keyword trigger
    for kw in HIGH_STAKES_KEYWORDS:
        if kw in text:
            reasons.append(f"Matched keyword: '{kw}'")
            break

    # Weaker domain-based trigger (only if no strong keyword hit)
    if not reasons:
        domain_hits = [h for h in DOMAIN_HINTS if h in text]
        if domain_hits:
            reasons.append(
                f"Domain hint(s): {', '.join(sorted(set(domain_hits)))}"
            )

    is_high_stakes = len(reasons) > 0
    return TriggerResult(
        is_high_stakes=is_high_stakes,
        reasons=reasons,
    )
