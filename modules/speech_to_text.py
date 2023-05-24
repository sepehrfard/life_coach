import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        audio = recognizer.listen(source)

    try:
        print('Recognizing...')
        text = recognizer.recognize_google(audio, language='en-us')
        print('You said: ' + text)
        return text
    except Exception as e:
        print(str(e))
