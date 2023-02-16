import openai
import config


def get_response(prompt, cxt=None):
    openai.api_key = config.openai_key
    completions = openai.Completion.create(
        engine="text-davinci-003",
        # engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        # context=cxt,
    )
    message = completions.choices[0].text
    return message.strip()

# while True:
#     user_input = input("User: ")
#     response = get_response(user_input)
#     print("Bot: ", response)