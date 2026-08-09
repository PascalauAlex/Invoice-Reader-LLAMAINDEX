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


📤 Expected Output

The script will process the PDF and print a structured JSON response containing the extracted data:
{
  "vendor": "Acme Corp",
  "invoice_date": "2023-10-15T00:00:00",
  "due_date": "2023-11-15T00:00:00",
  "invoice_number": "INV-10293",
  "total_due": "$1,250.00",
  "items": [
    "Web Design Services",
    "Hosting for 1 year"
  ]
}
