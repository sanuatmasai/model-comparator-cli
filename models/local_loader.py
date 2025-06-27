# models/local_model.py
from transformers import pipeline

# Define local model mapping
model_map = {
    "base": "gpt2",  # Small base model
    "instruct": "google/flan-t5-base",  # Instruction-tuned
    "finetuned": "tiiuae/falcon-7b-instruct"  # Example fine-tuned model (must be downloaded first)
}

# Cache pipelines to avoid reloading each time
loaded_pipelines = {}

def query_local_model(model_type, prompt):
    model_id = model_map.get(model_type, "gpt2")

    try:
        # Load the model pipeline only once per model
        if model_id not in loaded_pipelines:
            print(f"Loading model: {model_id} (this may take a while the first time)")
            pipe = pipeline("text-generation", model=model_id)
            loaded_pipelines[model_id] = pipe
        else:
            pipe = loaded_pipelines[model_id]

        # Run the prompt through the pipeline
        output = pipe(prompt, max_length=200, do_sample=True, temperature=0.7)[0]["generated_text"]

        return {
            "output": output.strip(),
            "model": model_id,
            "tokens_used": "N/A",  # Token count not directly available in pipeline
            "context_window": "Depends on model (e.g., GPT2 ~1024 tokens)"
        }

    except Exception as e:
        return {
            "output": f"Error loading or running model: {str(e)}",
            "model": model_id,
            "tokens_used": "N/A",
            "context_window": "Unknown"
        }
