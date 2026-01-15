class ResponseParser:
    """
    Parse raw LLM outputs into clean responses.
    """

    def parse(self, raw_text: str) -> str:
        if "Assistant:" in raw_text:
            return raw_text.split("Assistant:")[-1].strip()
        return raw_text.strip()
