import speech_recognition
from gtts import gTTS 
import os

voice=""

while True:
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        try:
            print(text)
            if text=="stop":
                break
            voice=voice+str(text)

            except:
                print("say something...") 

hr=gTTS(text=voice,lang='en', slow=False)
hr.save("1.wav")