import tkinter as tk
import speech_recognition as sr
import webbrowser as wb

r = sr.Recognizer()
r.pause_threshold = 3


def record():
    with sr.Microphone() as source:
        try:
            print("speak now ...")
            audio = r.listen(source)
            words = r.recognize_google(audio)
            print(words)
            f = open("Resources/notepad.txt", "a")
            f.write(words + '\n')
            f.close()
        except sr.UnknownValueError:
            print('try again !')
            record()


while True:
    val = input("press r to record, s to stop: ")
    if val == 'r':
        record()
    elif val == 's':
        break


