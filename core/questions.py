# core/questions.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class Question:
    key: str
    prompt: str


BASE_QUESTIONS: List[Question] = [
    Question(
        key="intent",
        prompt="What problem are you hoping this decision will solve?"
    ),
    Question(
        key="reversibility",
        prompt="If this decision turns out to be wrong, how hard would it be to undo in 6 months?"
    ),
    Question(
        key="cost",
        prompt="What becomes worse if this decision doesn’t work out as expected?"
    ),
]

FOLLOW_UPS: Dict[str, List[Question]] = {
    "deflection": [
        Question(
            key="deflection_clarify",
            prompt="I’m noticing your answer might be avoiding details. What’s one specific example that makes you say that?"
        ),
    ],
    "overconfidence": [
        Question(
            key="overconfidence_failcase",
            prompt="What’s the most realistic way this could go wrong, even if you’re confident?"
        ),
    ],
    "low_specificity": [
        Question(
            key="specificity_details",
            prompt="Can you answer with 2–3 concrete details (who/what/when) so it’s less vague?"
        ),
    ],
    "emotional": [
        Question(
            key="emotion_label",
            prompt="What emotion is driving this most right now, and what triggered it?"
        ),
    ],
    "irritation": [
        Question(
            key="irritation_recover",
            prompt=(
                "Got it — I may be pushing too fast. "
                "Let’s ground this with one concrete detail: what’s one real-world consequence if this decision goes wrong?"

            )
        ),
    ],
}
