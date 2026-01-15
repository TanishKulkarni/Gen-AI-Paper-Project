from enum import Enum
from memory.memory_item import MemoryItem

class MemoryAction(Enum):
    RETAIN = "retain",
    FORGET = "forget",
    COMPRESS = "compress"  # Placeholder for phase 4

class ForgettingPolicy:
    """
    Rule-Based selective forgetting policy.
    """

    def __init__(
            self,
            forget_threshold: float = 0.5,
            retain_threshold: float = 1.5
    ):
        self.forget_threshold = forget_threshold
        self.retain_threshold = retain_threshold

    def decide(self, memory: MemoryItem) -> MemoryAction:
        """
        Decide what to do with a memory.
        """

        if memory.importance < self.forget_threshold:
            return MemoryAction.FORGET
        
        if memory.importance >= self.retain_threshold:
            return MemoryAction.RETAIN
        
        return MemoryAction.RETAIN