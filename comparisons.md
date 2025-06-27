# 📊 Model Comparison Summary

This document compares outputs from **Base**, **Instruct**, and **Fine-tuned** models using 5 different prompts.

Each table shows the model’s output and a brief note on how well it performed.

---

## 🧪 Prompt 1: "Explain gravity like I'm 5."

| Model Type   | Output Snippet                                           | Comment                              |
|--------------|----------------------------------------------------------|--------------------------------------|
| Base (GPT-2) | "Gravity is a force... apples fall... mass..."           | Factual but robotic tone             |
| Instruct     | "Imagine you're holding a ball. Gravity pulls it down!" | Clear, child-friendly explanation    |
| Fine-tuned   | "Gravitational pull results from mass and energy..."    | Too complex for a child              |

✅ **Best Model:** Instruct

---

## 💼 Prompt 2: "Summarize a legal contract in plain English."

| Model Type   | Output Snippet                                             | Comment                                 |
|--------------|------------------------------------------------------------|-----------------------------------------|
| Base         | "Agreement... party... conditions..."                      | Disorganized, lacks summary logic      |
| Instruct     | "This contract is about services being exchanged..."       | Decent summary, not fully accurate     |
| Fine-tuned   | "This agreement ensures that party A provides..."          | Precise, legally accurate and clear    |

✅ **Best Model:** Fine-tuned

---

## 🎨 Prompt 3: "Write a short poem about the moon."

| Model Type   | Output Snippet                            | Comment                           |
|--------------|---------------------------------------------|-----------------------------------|
| Base         | "Moon in the sky, floating by..."           | Creative, poetic tone             |
| Instruct     | "The moon shines bright at night..."        | Simple, structured poem           |
| Fine-tuned   | "The moon as described in physics..."       | Off-topic, factual instead        |

✅ **Best Model:** Base

---

## 👩‍🔬 Prompt 4: "Explain photosynthesis in simple terms."

| Model Type   | Output Snippet                                      | Comment                              |
|--------------|-----------------------------------------------------|--------------------------------------|
| Base         | "Plants use light to make food..."                 | Informative, slightly unclear        |
| Instruct     | "Plants are like little chefs. They cook using sun!"| Great metaphor, engaging for kids    |
| Fine-tuned   | "Photosynthesis is the process of converting..."   | Accurate but very technical          |

✅ **Best Model:** Instruct

---

## 🧑‍💻 Prompt 5: "Fix this code: print('Hello' + 5)"

| Model Type   | Output Snippet                                  | Comment                            |
|--------------|--------------------------------------------------|------------------------------------|
| Base         | "print('Hello' + 5)"                            | Just repeated the input            |
| Instruct     | "Use str(): print('Hello' + str(5))"            | Correct fix with explanation       |
| Fine-tuned   | "The error occurs because..."                   | Detected issue, gave fix and reason|

✅ **Best Model:** Instruct / Fine-tuned (tie)

---

## 🧠 Insights & Recommendations

| Use Case              | Best Model Type |
|-----------------------|-----------------|
| General Q&A / Teaching| Instruct        |
| Creative Writing      | Base            |
| Specialized Tasks     | Fine-tuned      |
| Debugging / Coding    | Instruct        |
| Legal / Medical Use   | Fine-tuned      |

---

This summary helps guide **when and why** to use different LLM model types effectively.
