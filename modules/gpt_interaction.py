import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


# Example of what yesterday summary could look like:
YESTERDAY_SUMMARY = """
Things that happened:
- Had a meeting with their boss, and he said they were doing a great job.
- Broke up with their co-founder and felt really sad about it.
- Girlfriend is coming to visit this weekend. Very excited about getting together with her again.
- Need to prioritize some physical activity. Body is feeling stiff and sore from sitting all day.
"""

SYSTEM_PROMPT = """you are a helpful assistant. Every morning your job is to ask the user about what they have going on in their day given the summary of yesterday’s morning and night calls with the user about everything going on in their life.
Yesterday summary: {summary}
- You are to follow up on things they bring up in conversation
- Remind them of the achievement of Yesterdays if they seem down or stressed
- Remind them of their hectic yesterday if they don’t feel great today.
"""

def get_response(user_input, messages):
    messages.append({"role": "user", "content": user_input})

    chat = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
    )

    messages.append({"role": "assistant", "content": chat['choices'][0]['message']['content']})
    response_text = chat['choices'][0]['message']['content']

    return response_text, messages
