from typing import List
from .memory_item import MemoryItem

class MemoryStore:
    """
    Stores episodic and semantic memories
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
    
    def get_by_type(self, memory_type: str) -> List[MemoryItem]:
        return [m for m in self.memories if m.memory_type == memory_type]
    
    def size(self) -> int:
        """
        Number of stored memories.
        """
        return len(self.memories)