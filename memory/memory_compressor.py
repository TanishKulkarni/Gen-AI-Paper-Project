import re
from typing import List
from memory.memory_item import MemoryItem


class MemoryCompressor:
    """
    Compresses episodic memories into structured semantic memory.
    """

    def __init__(self, compression_threshold: float = 0.8):
        self.compression_threshold = compression_threshold

    def compress(self, memories: List[MemoryItem]) -> List[MemoryItem]:
        episodic = [
            m for m in memories
            if m.memory_type == "episodic"
            and m.importance < self.compression_threshold
        ]

        if not episodic:
            return []

        facts = self.extract_facts(episodic)
        if not facts:
            return []

        semantic_memories = []
        for fact in facts:
            semantic_memories.append(
                MemoryItem(
                    content=fact,
                    embedding=None,
                    memory_type="semantic",
                    importance=2.0
                )
            )

        return semantic_memories

    def extract_facts(self, memories: List[MemoryItem]) -> List[str]:
        """
        Extract structured facts from episodic memories.
        """
        facts = []

        for m in memories:
            text = m.content.lower()

            # Name extraction
            match = re.search(r"my name is (\w+)", text)
            if match:
                name = match.group(1)
                facts.append(f"FACT: User name is {name}")

        return list(set(facts))
