from openai import OpenAI
import dotenv
CFG = dotenv.dotenv_values(".env")

client = OpenAI(api_key=CFG["DS_API_KEY"], base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "What is the capital of the United States?"},
    ],
    stream=False
)

print(response.choices[0].message.content)