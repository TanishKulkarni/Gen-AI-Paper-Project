from typing import List 
from memory.memory_item import MemoryItem
from memory.importance_tracker import ImportanceTracker
from memory.forgetting_policy import ForgettingPolicy, MemoryAction

class MemoryController:
    """
    Controls memory lifecycle decisions.
    """

    def __init__(
            self,
            importance_tracker: ImportanceTracker,
            forgetting_policy: ForgettingPolicy
    ):
        self.importance_tracker = importance_tracker
        self.forgetting_policy = forgetting_policy

    def update_memories(
            self,
            memories: List[MemoryItem]
    ) -> List[MemoryItem]:
        """
        Apply importance updates and selective forgetting.
        """

        updated_memories = []

        for memory in memories:
            # Update importance
            self.importance_tracker.update(memory)

            # Decide action
            action = self.forgetting_policy.decide(memory)

            if action == MemoryAction.RETAIN:
                updated_memories.append(memory)

            elif action == MemoryAction.FORGET:
                continue # Drop Memory

            elif action == MemoryAction.COMPRESS:
                # Placeholder for phase 4
                updated_memories.append(memory)

        return updated_memories