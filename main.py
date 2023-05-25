from modules.speech_to_text import speech_to_text
from modules.text_to_speech import text_to_speech
from modules.gpt_interaction import get_response
from dotenv import load_dotenv
load_dotenv()

def main():
    while True:
        user_speech = speech_to_text()
        response_text = get_response(user_speech)
        text_to_speech(response_text)

if __name__ == '__main__':
    main()
