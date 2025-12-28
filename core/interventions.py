from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass(frozen=True)
class Intervention:
    id: str
    type: str                    # clarification, constraint, grounding, etc.
    target_failure: Optional[str]
    cognitive_state_before: str
    question_text: str
    timestamp: datetime
