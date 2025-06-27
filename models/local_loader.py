"""
Local model loader for the Model Comparator CLI
"""
from typing import Dict, Any, Optional
import torch
from pathlib import Path

class LocalModelLoader:
    def __init__(self, model_path: str, **kwargs):
        self.model_path = Path(model_path)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = None
        self.tokenizer = None
    
    def load_model(self):
        """Load the model and tokenizer from local path"""
        try:
            # This is a simplified example - actual implementation will depend on the model type
            from transformers import AutoModelForCausalLM, AutoTokenizer
            
            self.tokenizer = AutoTokenizer.from_pretrained(str(self.model_path))
            self.model = AutoModelForCausalLM.from_pretrained(
                str(self.model_path),
                device_map="auto",
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
            )
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    
    def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Generate text using the loaded model"""
        if not self.model or not self.tokenizer:
            return {"error": "Model not loaded. Call load_model() first."}
        
        try:
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=kwargs.get("max_tokens", 100),
                temperature=kwargs.get("temperature", 0.7),
                do_sample=True
            )
            
            generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return {
                "content": generated_text,
                "usage": {"input_tokens": inputs.input_ids.shape[1]}
            }
        except Exception as e:
            return {"error": str(e)}
