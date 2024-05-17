from g4f.client   import Client
from g4f.Provider import You


llm_model = "gpt-3.5-turbo"

client = Client(provider=You)

def get_completion(prompt, model=llm_model):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    # print(response.choices[0].message.content or "")

    # print(response.choices)
    return response.choices[0].message.content or ""

print(get_completion("What is 1+1?"))