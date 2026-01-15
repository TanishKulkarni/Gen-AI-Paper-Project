from typing import List
from .memory_item import MemoryItem

class MemoryStore:
    """
    Simple in-memory storgae for MemoryItem objects.
    """

    def __init__(self):
        self.memories: List[MemoryItem] = []

    def add(self, memory: MemoryItem):
        """
        Add a memory to the store.
        """ 
        self.memories.append(memory)

    def get_all(self) -> List[MemoryItem]:
        """
        Return all memories.
        """
        return self.memories
    
    def size(self) -> int:
        """
        Number of stored memories.
        """
        return len(self.memories)