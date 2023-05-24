import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(user_input):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",  # Update this to the GPT-4 model when it's released
      messages=messages
    )

    return response.choices[0].message['content']
