# 🤖 Model Comparison CLI Tool

A simple command-line tool to compare **Base**, **Instruct**, and **Fine-tuned** language models from **OpenAI**, **Hugging Face**, and **local models**.

This tool helps developers and learners understand how different model types behave when given the same prompt.

---

## 📦 Features

- Compare outputs from Base, Instruct, and Fine-tuned models
- Supports OpenAI, Hugging Face, and locally downloaded models
- View token usage and context window info
- Lightweight and easy to extend

---

## 🚀 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/yourname/model-comparator-cli.git
cd model-comparator-cli
```

### 2. Create Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add API Keys
- Create a `.env` file in the root folder.
- Add the following (see `.env.example`):

```env
OPENAI_API_KEY=your-openai-key
HF_API_KEY=your-huggingface-key
```

---

## 🛠️ Usage

### 📘 Basic Command
```bash
python main.py --provider openai --model_type instruct --prompt "Explain gravity like I'm 5."
```

### 🧠 Arguments
| Argument        | Description                            | Values                        |
|----------------|----------------------------------------|-------------------------------|
| `--provider`    | Model provider                         | `openai`, `huggingface`, `local` |
| `--model_type`  | Type of model                          | `base`, `instruct`, `finetuned` |
| `--prompt`      | Your input prompt                      | "your text here"             |

---

## 📁 Folder Structure
```
model-comparator-cli/
├── main.py
├── models/
│   ├── openai.py
│   ├── huggingface.py
│   └── local_model.py
├── .env.example
├── README.md
├── comparisons.md
└── requirements.txt
```

---

## ✅ Example
```bash
python main.py --provider huggingface --model_type instruct --prompt "Summarize the French Revolution."
```
```
=== Model Output ===
The French Revolution was a period of...

=== Model Info ===
Model: google/flan-t5-base
Type: Instruct
Token usage: N/A
Context window: ~1024–4096 tokens depending on model
```

---

## 📌 Notes
- Make sure local models are downloaded if you're using `local` provider.
- OpenAI fine-tuned model name can be set in `.env` using `OPENAI_FINE_TUNED_MODEL`
- Hugging Face fine-tuned model can be set with `HF_FINE_TUNED_MODEL`

---

## 📜 License
MIT License. Free to use and modify.
