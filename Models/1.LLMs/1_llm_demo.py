from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = GoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.9, max_completion_tokens=10)
response = llm.invoke("Hello, how are you?")
print(response)
