import speech_recognition as sr

# Initialize recognizer and microphone
recognizer = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()
print("Available microphones:")
for i, mic_name in enumerate(mic_list):
    print(f"{i}: {mic_name}")
# Prompt user to select a microphone
mic_index = int(input("Select a microphone: "))
mic = sr.Microphone(device_index=mic_index)


def speech_to_text():
    with mic as source:
        print(f"Listening from {mic_list[mic_index]}...")
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio, language="en-us", show_all=False)
            text = str(text)
            print("You said: " + text)
            return text
        except Exception as e:
            print(str(e))
