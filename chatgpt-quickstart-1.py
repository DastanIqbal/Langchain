from g4f.client   import Client
from g4f.Provider import You
# from g4f.gui import run_gui
# run_gui()

client = Client(provider=You)
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}],
)

print(chat_completion.choices[0].message.content or "")


# response = client.images.generate(
#   model="gemini",
#   prompt="a white siamese cat",
# )
# image_url = response.data[0].url

