from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="ggemini-3.6-flash")
response = model.invoke("Hello, how are you?")
print(response.content)
