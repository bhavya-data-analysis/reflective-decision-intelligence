# core/profile.py
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class DecisionProfile:
    decision_text: str
    clarity: str
    fragility: int
    reflection_depth: int
    signals: Dict[str, int]
    reflection_effect: Optional[str] = None
