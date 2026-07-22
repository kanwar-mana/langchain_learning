from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model="claude-4.5-sonnet", temperature=0.8, max_completion_tokens=10)
response = model.invoke("Hello, how are you?")
print(response.content)
