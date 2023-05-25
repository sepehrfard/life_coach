import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    # Print list of available microphones
    mic_list = sr.Microphone.list_microphone_names()
    print('Available microphones:')
    for i, mic_name in enumerate(mic_list):
        print(f'{i}: {mic_name}')

    # Prompt user to select a microphone
    # mic_index = int(input('Select a microphone: '))
    mic_index = 4

    with sr.Microphone(device_index=mic_index) as source:
        print(f'Listening from {mic_list[mic_index]}...')
        audio = recognizer.listen(source)

    try:
        print('Recognizing...')
        text = recognizer.recognize_google(audio, language='en-us', show_all=False)
        text = str(text)
        print('You said: ' + text)
        return text
    except Exception as e:
        print(str(e))