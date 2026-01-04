# core/triggers.py
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class TriggerResult:
    is_high_stakes: bool
    reasons: List[str]


# =========================
# Strong irreversible triggers
# =========================
HIGH_STAKES_KEYWORDS: Tuple[str, ...] = (
    # Career / income (irreversible)
    "quit", "quitting", "resign", "resignation",
    "leave my job", "leave job",
    "drop out", "dropout",
    "fire", "fired", "layoff", "laid off",

    # Location / immigration
    "leave country", "leaving country",
    "move abroad", "moving abroad",
    "go back to my country", "return to my country",
    "immigrate", "immigration", "emigrate", "visa",

    # Relationships (irreversible)
    "break up", "divorce",
    "marry", "marriage",

    # Assets / finance (hard to undo)
    "sell my house", "buy a house",
    "take a loan", "loan", "debt", "mortgage",

    # Health
    "surgery", "operation",
)


# =========================
# Domains (context only)
# =========================
DOMAIN_HINTS: Tuple[str, ...] = (
    # Work / career
    "job", "career", "company", "manager", "work",

    # Business
    "business", "startup", "side business", "ecom",

    # Relationships
    "relationship", "family", "girlfriend", "boyfriend",

    # Money
    "money", "finance", "rent", "salary", "income",

    # Health
    "health", "doctor",

    # Location
    "move", "relocate", "city", "country",
)


# =========================
# Risk amplifiers (new)
# =========================
RISK_AMPLIFIERS: Tuple[str, ...] = (
    # Financial downside
    "no income", "unstable", "risk", "lose money",
    "bankrupt", "loss", "debt", "loan", "mortgage",

    # Irreversibility signals
    "no backup", "no plan b", "all in", "everything",
    "cannot undo", "hard to undo",

    # Responsibility signals
    "kids", "family depends", "wife", "husband",
)


def detect_high_stakes(decision_text: str) -> TriggerResult:
    text = (decision_text or "").strip().lower()
    reasons: List[str] = []

    # 1️⃣ Strong keyword trigger (always high-stakes)
    for kw in HIGH_STAKES_KEYWORDS:
        if kw in text:
            reasons.append(f"Matched irreversible keyword: '{kw}'")
            return TriggerResult(True, reasons)

    # 2️⃣ Domain + risk amplifier (conditional)
    domain_hits = [h for h in DOMAIN_HINTS if h in text]
    risk_hits = [r for r in RISK_AMPLIFIERS if r in text]

    if domain_hits and risk_hits:
        reasons.append(
            f"Domain + risk: {', '.join(sorted(set(domain_hits)))} "
            f"| risk: {', '.join(sorted(set(risk_hits)))}"
        )
        return TriggerResult(True, reasons)

    # 3️⃣ Otherwise: not high-stakes
    return TriggerResult(False, [])
