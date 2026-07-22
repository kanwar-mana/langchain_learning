from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv
load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=300)

document = [
"Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
"MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
"Sachin Tendulkar, also known as the 'God of Critket', holds many batting records.",
"Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
"Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query="tell me about virat kohli"

document_embeddings=embedding.embed_documents(document)
query_embeddings=embedding.embed_query(query)

scores=cosine_similarity([query_embeddings], document_embeddings)[0]


index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(query)
print("\n")
print(document[index])
print("\nSimilarity Score: ",score)