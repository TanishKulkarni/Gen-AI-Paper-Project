from enum import Enum
from memory.memory_item import MemoryItem


class MemoryAction(Enum):
    RETAIN = "retain"
    FORGET = "forget"
    COMPRESS = "compress"


class ForgettingPolicy:
    """
    Selective forgetting + compression policy.
    """

    def __init__(
        self,
        forget_threshold: float = 0.5,
        compress_threshold: float = 0.8,
        retain_threshold: float = 1.5
    ):
        self.forget_threshold = forget_threshold
        self.compress_threshold = compress_threshold
        self.retain_threshold = retain_threshold

    def decide(self, memory: MemoryItem) -> MemoryAction:

        if memory.importance < self.forget_threshold:
            return MemoryAction.FORGET

        if memory.importance < self.compress_threshold:
            return MemoryAction.COMPRESS

        return MemoryAction.RETAIN
