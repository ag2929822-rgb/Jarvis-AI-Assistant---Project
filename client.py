from openai import OpenAI
client = OpenAI(
    api_key ="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",
)

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are virtual assitant name Jarvis skilled general task like alexa and google cloud."},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)
