from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model = "llama3.2",temperature =0)

prompts = ChatPromptTemplate.from_template("""
You are an expert Prompt Enhancer.

Your task is to transform the user's input into a clear,
specific, well-structured, and effective prompt for an LLM.

The input may contain broken English, incomplete sentences,
vague instructions, or only a single line.

Follow these instructions:

1. Understand the user's original intent.
2. Correct grammar and improve clarity.
3. Identify the appropriate role for the LLM.
4. Add relevant context based on the user's input.
5. Define a clear and specific task.
6. Specify the expected output structure or format.
7. Include relevant constraints and requirements.
8. Do not invent information or change the user's intent.
9. If essential information is missing, use placeholders
   such as [insert topic] instead of making assumptions.
10. Keep the optimized prompt detailed enough to be useful,
    but avoid unnecessary instructions.

Structure the optimized prompt using these sections:

Role:
Define who the LLM should act as.

Context:
Explain the relevant background and purpose.

Task:
Describe exactly what the LLM should do.

Requirements:
List important instructions and constraints.

Output Format:
Specify how the response should be structured.

Input Prompt:
{prompt}

Return only the optimized prompt.
Do not answer the original prompt or explain your changes.

Optimized Prompt:
""")