## Core components 

1. models
2. prompts 
3. chains 
4. memory 
5. indexe
6. agents 

## Modesl
Models are the core interfaces through which you interact with ai models
big problems of NLP based systems:
LLms solved both the NLU and context aware text generation problems 

issue: llms models are huge because of which normal ppl and companies cant use it 
solution : api based use 

third problem : Implementation standardization challenge 
code that you have to write to communicate with claude vs chatgpt are different and its hard to track and maintain
- developed interface to do this 

## LangChain: OpenAI vs Claude (Anthropic)

### OpenAI (GPT)

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4",
    temperature=0
)

result = model.invoke("Now divide the result by 1.5")

print(result.content) 
```
##  Claude (Anthropic)
```python
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-3-opus-20240229"
)

result = model.invoke("Hi, who are you?")

print(result.content)
```

Langchain : 2 types of model s
1. Langugae models 
LLMs , take text input and output text 

2. Embedding modesl 
text input --> vector output 
main use case is semantic search 

dcos for chat and embeddings
https://docs.langchain.com/oss/python/integrations/chat 
https://docs.langchain.com/oss/python/integrations/embeddings


## 2. Prompts 

LLm ---> input ---> prompt 
types: 
### 1. Dynamic & Reusable Prompts

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Summarize {topic} in a {emotion} tone"
)

print(prompt.format(topic="Cricket", emotion="fun"))
```
### 2. Role based prompts 
from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an experienced {profession}"),
    ("user", "Tell me about {topic}")
])

messages = chat_prompt.format_messages(
    profession="Doctor",
    topic="Viral Fever"
)

print(messages)

### 3 . few short prompting 
```python
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

# Examples
examples = [
    {"input": "Charged twice this month", "output": "Billing Issue"},
    {"input": "App crashes on login", "output": "Technical Problem"},
    {"input": "How to upgrade plan?", "output": "General Inquiry"},
]

# Example format
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Ticket: {input}\nCategory: {output}\n"
)

# Few-shot prompt
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Classify tickets: Billing Issue | Technical Problem | General Inquiry\n",
    suffix="Ticket: {user_input}\nCategory:",
    input_variables=["user_input"],
)

output 
```bash
classify tickets....

ticket: i was charged twice for my subscription this month
category : billing issue 
```

## Chains (very important )
can be used to build pipelines
prev stage output = next stage input
can be used to build complex pipelines
1. parallel chain (input fed into 2 llms parallely and teh output is combined)
2. conditional chain (example input-> process --- (if good type of feedback say thankyou and save, else mail it to the customer support team))

## 4. Indexes 
indexes connect your application to external knowledge such as pdfs websites or databases 
it has doc loader, text splitter, vectore store, retrievers , embeddings

## 5  memory 
llm api calls are stateless

who is niccollus nasseeb taleb -- llm api -> reply 
how old is he ---->  llm api --> as an ai i dont have access to personal data (failed to decode he)
1. converstation buffer memeory : stores a trasncript of recent messages / great for short chats but can grow large quickly 
2. conversationbuffer window memory : only keeps the last n interations to avaoid excessive token usage 
3. summarizer based memory : periodically summarizes older chat segments to keep a condenssed memory footprint 
4. custom memory : for advanced use cases you can store specialized state eg the user's preferences or key facfts about them in a custom memory class 

## 6 agents 
agents have reasoning capabilities and access to some tools 
example : consider an agent with access to tools like calculator and weather api 
user: can you multiply todays temp of delthi with 3
reasoning can be done through so many techniques say chain of thoughts 
delhi temp : use the tool and fetch it 
output 25 deg cel 
this has to be multiplied now 
check tools : found calcualtor 
calculate(temp,3, *)
return the output 

