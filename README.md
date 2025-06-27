# Model Comparator CLI

A command-line tool to compare different LLM models (OpenAI, Anthropic, HuggingFace, and local models) by sending them the same prompt and analyzing their responses.

## Features

- Compare multiple LLM models side by side
- Support for OpenAI, Anthropic, HuggingFace, and local models
- Token counting and cost estimation
- Response time measurement
- Visualization of results
- Prompt templates for common tasks

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd model-comparator-cli
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy the example environment file and add your API keys:
   ```bash
   cp .env.example .env
   ```
   Then edit the `.env` file with your API keys.

## Usage

Basic usage:
```bash
python main.py --prompt "Your prompt here" --models gpt-3.5-turbo gpt-4 claude-3-opus
```

### Command Line Arguments

- `--prompt`: The prompt to send to the models (required)
- `--models`: List of models to compare (space-separated)
- `--template`: Use a predefined prompt template (see `prompts/prompt_templates.json`)
- `--params`: Additional parameters as JSON string
- `--visualize`: Show visualizations of the results

### Examples

Compare two models with a custom prompt:
```bash
python main.py --prompt "Explain quantum computing in simple terms" --models gpt-3.5-turbo gpt-4
```

Use a predefined template:
```bash
python main.py --template summarization --params '{"text":"Long text to summarize..."}' --models gpt-3.5-turbo claude-3-opus
```

## Configuration

### Environment Variables

Create a `.env` file in the project root with your API keys:

```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

### Prompt Templates

You can define custom prompt templates in `prompts/prompt_templates.json`. Each template should have a `system` and `user` message that can include placeholders.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
