"""
OpenAI model handler for the Model Comparator CLI
"""
import openai
from typing import Dict, Any

class OpenAIModel:
    def __init__(self, model_name: str = "gpt-3.5-turbo", **kwargs):
        self.model_name = model_name
        self.client = openai.OpenAI(**kwargs)
    
    def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Generate a completion using the OpenAI API"""
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return {
                "content": response.choices[0].message.content,
                "usage": dict(response.usage)
            }
        except Exception as e:
            return {"error": str(e)}
