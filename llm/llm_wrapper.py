import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class LLMWrapper:
    """
    Open-source LLM Wrapper using Hugging Face Transformers.
    """

    def __init__(self, model_name: str, device: str = 'cpu'):
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()
    
    def generate(
        self,
        prompt: str,
        max_new_tokens: int = 128,
        temperature: float = 0.7
    ) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                do_sample=True,
                eos_token_id=self.tokenizer.eos_token_id
            )
        return self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )