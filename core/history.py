# core/history.py
from dataclasses import dataclass, field
from typing import List, Dict
from collections import Counter

from .profile import DecisionProfile


@dataclass
class DecisionHistory:
    """
    Holds multiple DecisionProfiles and extracts behavioral patterns.
    """
    profiles: List[DecisionProfile] = field(default_factory=list)

    def add(self, profile: DecisionProfile) -> None:
        self.profiles.append(profile)

    def pattern_summary(self) -> Dict[str, int]:
        """
        Aggregates recurring cognitive signals across decisions.
        """
        signal_counter = Counter()

        for profile in self.profiles:
            for signal, weight in profile.signals.items():
                signal_counter[signal] += weight

        return dict(signal_counter)

    def fragility_trend(self) -> List[int]:
        return [p.fragility for p in self.profiles]

    def reflection_depth_trend(self) -> List[int]:
        return [p.reflection_depth for p in self.profiles]
