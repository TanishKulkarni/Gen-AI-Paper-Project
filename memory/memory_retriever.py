import numpy as np
from typing import List
from .memory_item import MemoryItem
from .memory_store import MemoryStore

class MemoryRetriever:
    """
    Retrieves relevant memories using cosine similarity.
    """
    def __init__(self, memory_store: MemoryStore):
        self.memory_store = memory_store

    @staticmethod
    def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    def retrieve(
            self,
            query_embedding: np.ndarray,
            top_k: int = 5
    ) -> List[MemoryItem]:
        
        memories = self.memory_store.get_all()
        if not memories:
            return []
        
        scored = []
        for memory in memories:
            score = self.cosine_similarity(
                query_embedding, memory.embedding
            )
            scored.append((score, memory))

        scored.sort(key=lambda x: x[0], reverse=True)
        top_memories = [m for _, m in scored[:top_k]]

        # Update usage statistics
        for memory in top_memories:
            memory.touch()

        return top_memories
