from modules.speech_to_text import speech_to_text
from modules.text_to_speech import text_to_speech
from modules.gpt_interaction import get_response, SYSTEM_PROMPT
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    yesterday_summary = input("Please enter a summary of yesterday's events (comma-separated):\n")
    summary_list = yesterday_summary.split(",")
    summary_bullet_list = "\n".join([f"- {s.strip()}" for s in summary_list])
    messages = [{"role": "system", "content": SYSTEM_PROMPT.format(summary=summary_bullet_list)}]

    text_to_speech("Hello, I am your personal agent! Thanks for sharing about yesterday. Let's get started!")
    while True:
        user_speech = speech_to_text()
        response_text, messages = get_response(user_speech, messages)
        text_to_speech(response_text)

if __name__ == "__main__":
    main()