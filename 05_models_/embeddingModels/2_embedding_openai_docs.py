from langchain_openai import OpenAiEmbeddings 
from dotenv import load_dotenv

load_dotenv()
embedding = OpenAiEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = ["deljhi is the capital of india", "rcb won last year","paris is the capital of france"]
result = embedding.embed_documents(documents)

print(str(result))
# outputs vectore of 32 dimensions (bigger the dimensions more details get captured)




