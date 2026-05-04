from langchain_openai import OpenAiEmbeddings 
from dotenv import load_dotenv

load_dotenv()
embedding = OpenAiEmbeddings(model='text-embedding-3-large', dimensions=32)

result = embedding.embed_query("delhi is the capital of india")

print(str(result))
# outputs vectore of 32 dimensions (bigger the dimensions more details get captured)




