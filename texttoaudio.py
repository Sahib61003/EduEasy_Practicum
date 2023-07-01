import pyttsx3
import keyboard

notes = open(r"C:\python\Practicum\Basic.txt", encoding='utf-8')

text = notes.readlines()

engine = pyttsx3.init()

for i in text:
    engine.say(i)
    engine.runAndWait()