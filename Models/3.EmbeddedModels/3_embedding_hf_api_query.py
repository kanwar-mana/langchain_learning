from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding=HuggingFaceEmbeddings(
    model_name="Qwen/Qwen2.5-7B",
)
response=embedding.embed_query("What is the capital of Pakistan?")
print(str(response))