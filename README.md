# AI Prompt Enhancer 🚀

An AI-powered Prompt Enhancer built with Python and LangChain that transforms rough, unclear, or poorly written prompts into clear, structured, and effective prompts for Large Language Models (LLMs).

## 📌 Project Overview

Writing effective prompts is important for getting useful responses from LLMs. However, users may provide incomplete sentences, broken English, vague instructions, or poorly structured prompts.

The AI Prompt Enhancer helps solve this problem by improving prompt clarity while preserving the user's original intent.

It also identifies ambiguous inputs and asks for clarification when essential information is missing instead of making unsupported assumptions.

## ✨ Features

- **Prompt Optimization:** Converts rough prompts into clear, well-structured prompts.
- **Grammar Correction:** Improves spelling, grammar, and readability.
- **Intent Preservation:** Maintains the original meaning and purpose of the user's input.
- **Smart Clarification:** Asks questions only when essential information is missing.
- **Structured Prompts:** Organizes prompts into relevant sections:
  - Role
  - Context
  - Task
  - Requirements
  - Output Format
- **Ambiguity Handling:** Avoids inventing tasks when the user provides only a vague topic.
- **Flexible Input:** Supports short sentences, long descriptions, and informal language.

## 🛠️ Technologies Used

- Python
- LangChain
- Large Language Models (LLMs)

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install langchain-core
```

Install the integration package required by your chosen LLM provider. For example, if you use OpenAI:

```bash
pip install langchain-openai
```

### 4. Configure environment variables

If your chosen model provider requires an API key, store it in an environment variable rather than hardcoding it in your source code.

Example for OpenAI:

```bash
OPENAI_API_KEY=your_api_key_here
```

## 🚀 How It Works

1. The user enters a prompt.
2. The LLM analyzes the user's intent.
3. The system determines whether the input is sufficiently clear.
4. If the intent is clear, the system generates an optimized prompt.
5. If essential information is missing, the system asks a clarification question.
6. The optimized prompt is returned to the user.

## 💡 Example

### Input

```text
explain machine learning simple with example
```

### Optimized Output

```text
Role:
Act as an experienced machine learning educator.

Context:
The audience is a beginner with little knowledge of
machine learning.

Task:
Explain machine learning in simple language.

Requirements:
- Avoid unnecessary technical jargon.
- Include an easy-to-understand real-world example.
- Explain how the example works.

Output Format:
1. Simple definition
2. How it works
3. Real-world example
4. Short summary
```

### Ambiguous Input

```text
Python
```

### Expected Output

```text
Clarification Needed:

What would you like to do with Python?

- Learn Python basics
- Build a Python project
- Debug Python code
- Understand a specific Python concept
```

## 📂 Project Structure

```text
ai-prompt-enhancer/
├── main.py
├── prompts.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

*Note: This is a suggested structure. Adjust it to match your actual implementation.*

## 🔮 Future Improvements

- Add a web interface using Streamlit or FastAPI.
- Support multiple LLM providers.
- Add prompt quality evaluation.
- Build automated tests for prompt optimization.
- Compare original and optimized prompts.
- Add prompt injection detection and security testing.

## ⚠️ Limitations

- The quality of optimized prompts depends on the underlying LLM.
- Ambiguous inputs may still require human clarification.
- Prompt optimization does not guarantee accurate or hallucination-free responses.
- API access may incur costs depending on the chosen provider.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Submit a pull request.

## 📄 License

Choose an appropriate open-source license for your project, such as the MIT License, if you want to allow broad reuse.

---

**Built with Python, LangChain, and LLMs.**
