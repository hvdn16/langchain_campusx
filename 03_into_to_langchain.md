# Langchain 
its an opensource framework for dev applications powered by LLMs

why do we need langchain?
lets say i wanted to develop an application where the user can upload a pdf and read it from the site also he can ask questoins related to the pdf only 

high level overview of the architecture 

User query----> semantic search --> pdf stored in database --result---> system query [pages + user query]---> brain ---> final outoput
User query --> System Query 


Brain should have NLP capabilities, and also have context aware text generation 

## Semantic Search  
Search based on the **meaning** of text, not exact words.
---
### 🔍 Example
**Query:**  
> How many books has Nassim Taleb written?
**Docs:**  
- Taleb paragraph  
- Warren Buffett paragraph  
- Naval Ravikant paragraph  
---
### ⚙️ Flow
- Convert query → embedding (vector)  
- Convert all docs → embeddings  
- Compare similarity (e.g., cosine)  
- Pick closest match → **Taleb doc**

## Analysis 
Pdf ---upload ----aws s3---docs loader---->  Text splitter ---> page 1, page2 page3, page k----> mapped to embedding1 , embedding 2, embedding 3....embedding k -----> Database 

User query ---embedding in n dimensions -----> semantic search [Uses the Database and the embeddings of the pdf] ----> system query [pages+ user query ] ----> Brain [NLU + context aware text gen] ---> final output 

## Challenges in this project 
problem 1
- developing the brain  
- generating the relevant output 
 solution : use an LLM

 problem 2 
- computation and cost management 
solution : API's provided by the companies

problem 3 
- orchestration of these moving componetns 
in this aws s3 integration , text splitter, embeddings, db , llm , retrieval 
tasks : uploading, doc loader, embedding, db mgmt, retrieve, fetch final output 
it could take a long time to develop this from scratch also if something changes then its very challenging to adapt 
solution : Architecture 

## Benefits of langchain 
1. concept of chains : form a pipeline between tasks and components 
    differnt types of chains possibel 

2. Model agnostic development 
3. complete environment (doc loading, embedding etc..)
4. memory and state handling (in conversation memory)

## what can you build?
conversational chatbots, ai knowledge assistants , ai agents , workflow automation, summarization/research helpers 

## alternatives 
llama index
haystack 

