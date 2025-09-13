import os

from groq import Groq
prompt = input("Запитайте мене щось \n")
client = Groq(
    api_key=("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"),
)
def generate(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",
    )
    return chat_completion.choices[0].message.content
print(generate(prompt))