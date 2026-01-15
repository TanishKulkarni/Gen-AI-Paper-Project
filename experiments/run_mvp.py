import yaml
from llm.llm_wrapper import LLMWrapper
from llm.response_parser import ResponseParser
from sentence_transformers import SentenceTransformer
from memory.memory_item import MemoryItem
from memory.memory_store import MemoryStore
from memory.memory_retriever import MemoryRetriever
from memory.importance_tracker import ImportanceTracker
from memory.forgetting_policy import ForgettingPolicy
from controller.memory_controller import MemoryController



def load_config(path="configs/default.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def main():
    config = load_config()

    encoder = SentenceTransformer("all-MiniLM-L6-v2")
    memory_store = MemoryStore()
    retriever = MemoryRetriever(memory_store)
    importance_Tracker = ImportanceTracker(
        decay_rate=0.0005,
        usage_boost=0.05
    )

    forgetting_policy = ForgettingPolicy(
        forget_threshold=0.5,
        retain_threshold=1.2
    )

    memory_controller = MemoryController(
        importance_Tracker,
        forgetting_policy
    )

    FORGET_THRESHOLD = 0.5

    llm = LLMWrapper(
        model_name=config["llm"]["model_name"],
        device=config["runtime"]["device"]
    )

    parser = ResponseParser()

    print("\nSelective Memory-Augmented LLM (Phase 1: Basic Memory)")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        # Encode user input
        user_embedding = encoder.encode(user_input, normalize_embeddings=True)

        # Retrieve past memories
        past_memories = retriever.retrieve(user_embedding, top_k=3)

        # Build memory context
        memory_context = ""
        if past_memories:
            memory_context = (
                "You have access to the following past interactions.\n"
                "Use them to answer the user's question if relevant.\n\n"
            )
            for m in past_memories:
                memory_context += f"- {m.content}\n"
                importance_Tracker.update(m)

        # Build prompt
        prompt = (
            "You are a helpful assistant.\n\n"
            f"{memory_context}\n"
            f"User: {user_input}\n"
            "Assistant:"
        )

        raw_output = llm.generate(
            prompt,
            max_new_tokens=config["llm"]["max_new_tokens"],
            temperature=config["llm"]["temperature"]
        )

        response = parser.parse(raw_output)
        print(f"Assistant: {response}")

        # Store interaction as memory
        new_memory = MemoryItem(
                content=f"User: {user_input} | Assistant: {response}",
                embedding=user_embedding
            )
        memory_store.add(new_memory)

        # Apply importance decay + forgetting
        memory_store.memories = memory_controller.update_memories(
            memory_store.get_all()
        )

        # Console logs for the debugging

        print(f"[Memory size: {memory_store.size()}]\n"
              f"Avg importance: {sum(m.importance for m in memory_store.get_all()) / max(1, memory_store.size()):.2f}]"
              )


if __name__ == "__main__":
    main()
