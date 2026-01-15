from dataclasses import dataclass, field
from typing import Any
import time
import uuid

@dataclass
class MemoryItem:
    """
    Atomic memory unit stored in the system.
    """

    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    content: str = ""
    embedding: Any = None

    # Metadata (used later)
    timestamp: float = field(default_factory=time.time)
    usage_count: int = 0

    def touch(self):
        """
        Called whenever this memory is retrieved.
        """
        self.usage_count += 1