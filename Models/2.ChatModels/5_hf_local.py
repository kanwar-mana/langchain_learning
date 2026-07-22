from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFacePipeline(
    model_id="Qwen/Qwen2.5-72B-Instruct",
    model_kwargs=dict(
        task="text-generation",
        temperature=0.8,
        max_new_tokens=100
    )
)
model=ChatHuggingFace(llm=llm)
response=model.invoke("What is the capital of Pakistan?")
print(response.content)