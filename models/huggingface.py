# models/huggingface.py
import os
import requests

# Load Hugging Face API key from environment variable
HF_API_KEY = os.getenv("HF_API_KEY")

# Map model types to hosted model endpoints
model_map = {
    "base": "gpt2",  # Small base model
    "instruct": "google/flan-t5-base",  # Instruction-tuned model
    "finetuned": os.getenv("HF_FINE_TUNED_MODEL", "microsoft/phi-2")  # Replace with your fine-tuned model if available
}

def query_huggingface(model_type, prompt):
    model_id = model_map.get(model_type, "gpt2")
    api_url = f"https://api-inference.huggingface.co/models/{model_id}"

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}

    try:
        # Send POST request to Hugging Face Inference API
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # Extract generated text from response
        if isinstance(data, list) and "generated_text" in data[0]:
            output = data[0]["generated_text"]
        elif isinstance(data, dict) and "error" in data:
            output = f"Error: {data['error']}"
        else:
            output = str(data)

        return {
            "output": output.strip(),
            "model": model_id,
            "tokens_used": "N/A",  # Token count not returned in free tier
            "context_window": "~1024–4096 tokens depending on model"
        }

    except Exception as e:
        return {
            "output": f"Request failed: {str(e)}",
            "model": model_id,
            "tokens_used": "N/A",
            "context_window": "Unknown"
        }
