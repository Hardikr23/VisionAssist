from gtts import gTTS
from playsound import playsound

def text_to_speech(in_text):
    speech = gTTS(text = in_text)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')
    return True

in_text = "I am hardik's slave"
text_to_speech(in_text)