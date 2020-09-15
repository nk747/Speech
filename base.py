import speech_recognition as sr
import webbrowser as wb
from datetime import datetime


r = sr.Recognizer()

with sr.Microphone() as source:
    try:
        print("speak now...")
        audio = r.listen(source)
        words = r.recognize_google(audio)
    except sr.UnknownValueError:
        print('yadaa')


print(words)
query = words.replace(' ', '+')
url = f'https://www.google.com/search?q='
wb.open_new_tab(url + query)
