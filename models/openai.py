# models/openai.py
import os
import openai

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def query_openai(model_type, prompt):
    # Define model mapping for different types
    model_map = {
        "base": "davinci",  # Old base model (not instruction-tuned)
        "instruct": "gpt-3.5-turbo",  # Chat model tuned for instructions
        "finetuned": os.getenv("OPENAI_FINE_TUNED_MODEL", "ft:gpt-3.5:your-custom-model")
    }

    model = model_map.get(model_type, "gpt-3.5-turbo")

    # Send prompt to OpenAI model
    try:
        if model.startswith("gpt-"):  # Use ChatCompletion for instruct models
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            output = response.choices[0].message.content.strip()
            tokens_used = response.usage.total_tokens
        else:  # Use Completion API for base/fine-tuned legacy models
            response = openai.Completion.create(
                model=model,
                prompt=prompt,
                max_tokens=500,
                temperature=0.7
            )
            output = response.choices[0].text.strip()
            tokens_used = response.usage.total_tokens

        return {
            "output": output,
            "model": model,
            "tokens_used": tokens_used,
            "context_window": 4096  # Default context size for most OpenAI models
        }

    except Exception as e:
        return {
            "output": f"Error: {str(e)}",
            "model": model,
            "tokens_used": 0,
            "context_window": "Unknown"
        }
