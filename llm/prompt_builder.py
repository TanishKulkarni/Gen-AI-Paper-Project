class PromptBuilder:
    """
    Responsible for constructing prompts for the LLM.
    """

    def build(self, user_input: str) -> str:
        prompt = (
            "You are a helpful assistant.\n\n"
            f"User: {user_input}\n"
            "Assistant:"
        )
        return prompt