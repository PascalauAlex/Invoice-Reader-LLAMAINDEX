from llama_index.readers.file import PDFReader
from pathlib import Path
from pydantic import BaseModel
from datetime import datetime
from dotenv import load_dotenv
import os
from llama_index.llms.openai import OpenAI as client
import json

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")




class InvoiceData(BaseModel):
    vendor : str
    invoice_date : datetime
    due_date : datetime
    invoice_number : str
    total_due : str
    items : list[str]



pdfreader = PDFReader()
documents = pdfreader.load_data(file=Path("./data/invoice.pdf"))

text = documents[0].text 

llm = client(model="gpt-4o",api_key=openai_key)
# Returns a structured llm with the class definition inherited from pydantic BaseModel
sllm = llm.as_structured_llm(InvoiceData)

response = sllm.complete(text)

json_response = json.loads(response.text)
print(json.dumps(json_response, indent=2))
