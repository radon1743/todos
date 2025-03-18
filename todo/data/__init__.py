from dataclasses import dataclass
from datetime import datetime

@dataclass
class TodoData:
    """Todo data class"""

    date: datetime
    text: str
    completed: bool
    
