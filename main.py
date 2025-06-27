# main.py
import os
import argparse
from dotenv import load_dotenv

# Import model query functions from respective files
from models.openai import query_openai
from models.huggingface import query_huggingface
from models.local_model import query_local_model

def main():
    # Load environment variables from .env file (API keys, etc.)
    load_dotenv()

    # Setup command-line arguments
    parser = argparse.ArgumentParser(description="Compare LLMs: Base, Instruct, Fine-tuned")
    parser.add_argument("--provider", choices=["openai", "huggingface", "local"], required=True, help="Choose the model provider")
    parser.add_argument("--model_type", choices=["base", "instruct", "finetuned"], required=True, help="Choose the model type")
    parser.add_argument("--prompt", type=str, required=True, help="Enter your text prompt")
    args = parser.parse_args()

    print("\nRunning query...\n")

    # Route query to the appropriate model provider
    if args.provider == "openai":
        result = query_openai(args.model_type, args.prompt)
    elif args.provider == "huggingface":
        result = query_huggingface(args.model_type, args.prompt)
    elif args.provider == "local":
        result = query_local_model(args.model_type, args.prompt)
    else:
        print("Invalid provider.")
        return

    # Display model output and summary information
    print("=== Model Output ===")
    print(result["output"])
    print("\n=== Model Info ===")
    print(f"Model: {result['model']}")
    print(f"Type: {args.model_type.capitalize()}")
    print(f"Token usage: {result.get('tokens_used', 'N/A')}")
    print(f"Context window: {result.get('context_window', 'N/A')} tokens")

if __name__ == "__main__":
    main()
