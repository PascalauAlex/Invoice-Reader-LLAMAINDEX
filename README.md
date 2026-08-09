# 📄 AI Invoice Parser

A lightweight and efficient Python script that leverages **LlamaIndex**, **Pydantic**, and **OpenAI's GPT-4o** to automatically extract structured data from PDF invoices.

By defining a strict schema using Pydantic, the script guarantees that the LLM output is properly formatted and ready to be integrated into databases or other applications.

---

## ✨ Features

- **Automated PDF Parsing:** Reads and extracts text directly from PDF files.
- **Structured LLM Output:** Uses `as_structured_llm` to ensure the AI returns data matching a predefined Pydantic schema.
- **High Accuracy:** Powered by OpenAI's `gpt-4o` model.
- **JSON Export:** Outputs the extracted invoice data in a clean, strictly typed JSON format.

---

## 🛠️ Prerequisites

Before running the project, make sure you have the following installed:

- **Python 3.9+**
- An active **OpenAI API Key**

---

## 🚀 Installation & Setup

**1. Clone the repository or download the script**

**2. Install the required dependencies**
Run the following command to install the necessary Python packages:

```bash
pip install llama-index llama-index-llms-openai llama-index-readers-file pydantic python-dotenv
