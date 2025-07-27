from langchain_together import Together
import os
from dotenv import load_dotenv

load_dotenv()

llm = Together(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    api_key=os.getenv("TOGETHER_API_KEY"),
    temperature=0.5,
    max_tokens=512
)

prompt = "Give me a 2‑sentence motivational quote to start my day."

try:
    response = llm.invoke(prompt)
    print("✅ LLM response:\n", response)
except Exception as e:
    print("❌ ERROR:", e)
