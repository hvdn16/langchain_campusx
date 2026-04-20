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


