"""
HuggingFace model handler for the Model Comparator CLI
"""
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from typing import Dict, Any

class HuggingFaceModel:
    def __init__(self, model_name: str = "gpt2", **kwargs):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, **kwargs)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
        self.pipeline = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)
    
    def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Generate text using a local HuggingFace model"""
        try:
            result = self.pipeline(prompt, **kwargs)
            return {
                "content": result[0]["generated_text"],
                "usage": {"input_tokens": len(self.tokenizer.encode(prompt))}
            }
        except Exception as e:
            return {"error": str(e)}
