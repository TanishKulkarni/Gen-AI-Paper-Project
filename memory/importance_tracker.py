import time
from memory.memory_item import MemoryItem

class ImportanceTracker:
    """
    Updates importance scores and applies time decay.
    """

    def __init__(
            self,
            decay_rate: float = 0.01,
            usage_boost: float = 0.1
    ):
        self.decay_rate = decay_rate
        self.usage_boost = usage_boost
    
    def update(self, memory: MemoryItem):
        """
        Apply tmie decay and usage-based reinforcement.
        """
        now = time.time()

        # Time decay
        time_elapsed = now - memory.last_accessed
        decay = self.decay_rate * time_elapsed
        memory.importance = max(0.0, memory.importance - decay)

        # Usage reinforcement
        memory.importance += self.usage_boost * memory.usage_count

        # Update last accessed
        memory.last_accessed = now

    def should_forget(self, memory: MemoryItem, threshold: float) -> bool:
        """
        Decide whether a memory should be forgotten.
        """
        return memory.importance < threshold