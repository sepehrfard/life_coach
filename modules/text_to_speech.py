from gtts import gTTS
import simpleaudio as sa
from pydub import AudioSegment


def text_to_speech(text):
    tts = gTTS(text=text, lang="en, speed=1.2")
    tts.save("speech.mp3")
    sound = AudioSegment.from_mp3("speech.mp3")
    sound.export("speech.wav", format="wav")
    wave_obj = sa.WaveObject.from_wave_file("speech.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
