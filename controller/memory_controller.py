from typing import List
from memory.memory_item import MemoryItem
from memory.importance_tracker import ImportanceTracker
from memory.forgetting_policy import ForgettingPolicy, MemoryAction
from memory.memory_compressor import MemoryCompressor


class MemoryController:
    """
    Controls memory lifecycle decisions.
    """

    def __init__(
        self,
        importance_tracker: ImportanceTracker,
        forgetting_policy: ForgettingPolicy,
        compressor: MemoryCompressor
    ):
        self.importance_tracker = importance_tracker
        self.forgetting_policy = forgetting_policy
        self.compressor = compressor

    def update_memories(
        self,
        memories: List[MemoryItem]
    ) -> List[MemoryItem]:

        updated = []
        to_compress = []

        for memory in memories:
            self.importance_tracker.update(memory)
            action = self.forgetting_policy.decide(memory)

            if action == MemoryAction.RETAIN:
                updated.append(memory)
            elif action == MemoryAction.COMPRESS:
                to_compress.append(memory)
            elif action == MemoryAction.FORGET:
                continue

        # Apply compression
        semantic_memories = self.compressor.compress(to_compress)
        updated.extend(semantic_memories)

        return updated
