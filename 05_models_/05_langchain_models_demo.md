# what are models?
interfaces designed to facilitate interactions with various language models and embedding models 
if abstracts the complexity of working directly with different llms caht models and embedding models providing a uniform interface to communicate with them. this makes it easier to build application that rely on ai generated text , text embeddings for similarity search and Rag 

## plan of action 
1. language models (close source gpt models , claude and gemeni, and open source models from hugging face) : chat application
2. embedding models ( close source and open source from hugging face ): doc similarity application 

## Language models 
language modesl are ai systems designed to process generate and understand natural language text
language models : 1. llms 2. chat models 

l. llm general purpose modles that is used for raw text generation . they take a string or plain text as input and return a string (plaintext) these are traditionally older models and are not used much now 

2. chat models : language models that are specialized for conversational tasks . they take a sequence of messages as input and return chat messages as outputs (as opposed to using plain text). these are traditionally newer models and used more in comparision to the llms 



## LLMs vs Chat Models

## LLMs vs Chat Models

| Feature            | LLMs (Base Models)                               | Chat Models (Instruction-Tuned)                              |
|--------------------|-----------------------------------------------------|--------------------------------------------------------------|
| Purpose            | Free-form text generation                         | Optimized for multi-turn conversations                       |
| Training Data      | General text corpora (books, articles)            | Fine-tuned on chat datasets (dialogues, user-assistant)      |
| Memory & Context   | No built-in memory                                | Supports structured conversation history                     |
| Role Awareness     | No understanding of roles                         | Understands system, user, assistant roles                    |
| Example Models     | GPT-3, Llama-2-7B, Mistral-7B, OPT-1.3B           | GPT-4, GPT-3.5-turbo, Llama-2-Chat, Mistral-Instruct, Claude |
| Use Cases          | Text generation, summarization, translation, code | Chatbots, assistants, support, AI tutors                     |


## llm vs chat model 
llm : base model predict next token P(token| context), trained on large text corpora , no conecpt of chat roles or safety, raw flexible but uncontroled
chat model : llm + 4 layers
1. instruction tuning : trained on prompt ideal response pairs
2. rhlf (reinforcemnt learning human feedback...)
3. structured input format (instead of plain text uses roles)
4. tool/function calling (model can call apis run code fetch external data)


from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)
# OPENAI_API_KEY is set in the .env file, so we don't need to pass it here
llm.invoke("what is capital of karnataka?")
print(result)

## chatmodels 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# chatModels inherit from BaseLanguageModel, so they have all the same methods and properties
# llms inherit from BaseLanguageModel, so they have all the same methods and properties
# chatModels have some additional methods and properties that are specific to chat models

load_dotenv()
chat = ChatOpenAI(model="gpt-4", temperature=0.9)
# OPENAI_API_KEY is set in the .env file, so we don't need to pass it here
result = chat.invoke("what is capital of karnataka?")
print(result.content) 

### anthropic 
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv  
load_dotenv()
chat = ChatAnthropic(model="claude-2", temperature=0.9)
result = chat.invoke("what is capital of karnataka?")
print(result.content)

## gemini 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
chat = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest", temperature=1.9)
result = chat.invoke("what is capital of karnataka?")
print(result.content)

Temperature parameter 
In AI language models, **temperature** controls how predictable or creative the output is by adjusting how strongly the model favors the most likely next word. A **low temperature (e.g., 0.2)** makes responses more consistent and factual, while a **high temperature (e.g., 0.9)** produces more varied and creative but sometimes less accurate text.

**Examples:**

* Prompt: *“The sky is…”*

  * Low temperature (0.2): “The sky is blue.”
  * High temperature (0.9): “The sky is a swirling canvas of colors at dusk.”

* Prompt: *“Write a tagline for coffee”*

  * Low temperature: “Fresh coffee for your day.”
  * High temperature: “Awaken your soul with every bold, aromatic sip.”


## Working with open source models
opensource language models are freely available ai models that can be downloaded modified fine tuned and deployed without restrictions from a central provider 
unline closed source models such as open ais gpt 4 anthropics clausee or googles gemini opensource models allow full control and customization 

# Open-Source vs Closed-Source AI Models

## 🔍 Comparison

| Feature        | Open-Source Models                                      | Closed-Source Models                                      |
|---------------|----------------------------------------------------------|-----------------------------------------------------------|
| **Cost**      | Free to use (no API costs)                               | Paid API usage (e.g., OpenAI charges per usage)           |
| **Control**   | Can modify, fine-tune, and deploy anywhere               | Locked to provider's infrastructure                       |
| **Data Privacy** | Runs locally (no data sent to external servers)      | Sends queries to provider's servers                       |
| **Customization** | Can fine-tune on specific datasets                  | Limited or no fine-tuning access in most cases            |
| **Deployment** | Can be deployed on on-premise servers or cloud          | Must use vendor's API                                     |

---

## 🚀 Some Famous Open-Source Models

| Model           | Developer        | Parameters        | Best Use Case                          |
|-----------------|------------------|-------------------|----------------------------------------|
| LLaMA 2         | Meta AI          | 7B / 13B / 70B    | General-purpose text generation        |
| Mixtral 8x7B    | Mistral AI       | 8x7B (MoE)        | Efficient and fast responses           |
| Mistral 7B      | Mistral AI       | 7B                | Strong small-scale model               |
| Falcon          | TII (UAE)        | 7B / 40B          | High-speed inference                   |
| BLOOM           | BigScience       | 176B              | Multilingual text generation           |
| GPT-J           | EleutherAI       | 6B                | Lightweight and efficient              |
| GPT-NeoX        | EleutherAI       | 20B               | Large-scale applications               |

---

## 💡 Notes

- Open-source models are ideal for **research, customization, and privacy-sensitive applications**.
- Closed-source models are better suited for **ease of use, scalability, and production-ready APIs**.
- Compact models (like Mistral 7B) are great for **chatbots and low-resource environments**.

### where to find these models 
hugging face the largest repository of open source llms 

ways to use the open sourcec models 
1. using HF inference api
2. Running locally 


## Disadvantages 
High hardware requirements : running large models requires expensive gpus
setup complexity : installation of dependencies like pytorch cuda transformers etc 
lack of rhlf: most open srouce models dont havefine tuning with human feedback making them weaker in instruction following 
limited multimodal abilities : open models dont support images audio or video like gpt 4v 


## Coding 
create a token : HUGGINGFACEHUB_API_TOKEN and place it in .env
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.2-1B-Instruct',
    task='text-generation',
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("what is capital of karnataka?")
print(result.content)
available models  https://huggingface.co/models?pipeline_tag=text-generation&num_parameters=min:0,max:3B&inference_provider=all&sort=trending

## locally downloading 
# locally running huggingface models
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
llm = HuggingFacePipeline.from_model_id(
    model_id="google/gemma-3-1b-it",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 512, "temperature": 0.9},
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("what is capital of karnataka?, can you answer in kannada?")
print(result.content)

## chat model open ai 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)


# chat model anthropic 
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

result = model.invoke('What is the capital of India')

print(result.content)

# chat model google 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

result = model.invoke('What is the capital of India')

print(result.content)

# chat model hf api 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

result = model.invoke('What is the capital of India')

print(result.content)

# chatmodel hf local py 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

result = model.invoke('What is the capital of India')

print(result.content)




## Embedding models 

