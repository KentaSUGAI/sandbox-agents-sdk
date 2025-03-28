from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-search-preview",
    web_search_options={},
    messages=[
        {
            "role": "user",
            "content": "本日の明るいニュースを教えてください。",
        }
    ],
)

print(completion.choices[0].message.content)