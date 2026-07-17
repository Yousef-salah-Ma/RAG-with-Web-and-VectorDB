from model import load_model
from router import router 
from transformers import TextStreamer

model , tokenizer = load_model()

user_input = input("enter question")

prompt = [
    {
        "role": "system",
        "content": """
You are a routing assistant.

Your job is to choose ONE tool.

Available tools:

1. web_search
- Use for recent information, news, current events, and internet.

2. private_search
- Use for company documents, PDFs, manuals, and local knowledge.

Return ONLY one of:
web_search
private_search
"""
    },
    {
        "role": "user",
        "content": user_input
    }
]

token = tokenizer.apply_chat_template(prompt , return_tensors="pt")

outputs = model.generate(
    **token,
    max_new_tokens=20
)

new_tokens = outputs[0][token["input_ids"].shape[1]:]

response = tokenizer.decode(
    new_tokens,
    skip_special_tokens=True
).strip()

print(response.split()[1])

query =  user_input

context = router(response.split()[1], query)

messages = [
    {
        "role": "system",
        "content": """
You are a helpful AI assistant.

Answer the user's question using ONLY the provided context.

Rules:
- Do NOT use your own knowledge.
- If the answer is not in the context, say:
  "I couldn't find the answer in the provided context."
- Be concise and accurate.
"""
    },
    {
        "role": "user",
        "content": f"""
Context:
{context}

Question:
{query}
"""
    }
]
token = tokenizer.apply_chat_template(messages , return_tensors="pt")



streamer = TextStreamer(
    tokenizer,
    skip_prompt=True,
    skip_special_tokens=True
)

model.generate(
    **token,
    streamer=streamer,
    max_new_tokens=10000
)

