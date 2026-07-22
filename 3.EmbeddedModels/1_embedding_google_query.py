from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=10)
response=embedding.embed_query("What is the capital of Pakistan?")
print(str(response))