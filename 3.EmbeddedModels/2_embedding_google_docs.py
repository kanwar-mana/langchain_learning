from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

docs=["Hello World","What is the capital of Pakistan?","What is the capital of India?"]

embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=32)
response=embedding.embed_documents(docs)
print(str(response))
