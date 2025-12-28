from dataclasses import dataclass
from typing import Literal

Effect = Literal["helped", "no_change", "hurt"]

@dataclass
class InterventionAttribution:
    intervention_id: str
    delta_fragility: int
    effect: Effect
