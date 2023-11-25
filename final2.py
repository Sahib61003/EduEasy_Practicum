import tkinter as tk
import speech_recognition as sr
import googletrans
import pyttsx3
from vidstream import *
import socket
import threading

translator = googletrans.Translator()
engine = pyttsx3.init()

def speak(text):
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()

def translate_text():
    selected_language = language_var.get()

    recognizer = sr.Recognizer()

    speak("Speak now")

    # Recognize speech input
    with sr.Microphone() as source:
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language="en")
        print(text)

    translation = translator.translate(text, dest=selected_language)
    print(translation.text)

    #translated text to speech
    speak(translation.text)


def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()


def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), 3000)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()


def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0, 'end-1c'), 3000)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()


def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0, 'end-1c'), 2000)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()


local_ip_address = socket.gethostbyname(socket.gethostname())
print(local_ip_address)

server = StreamingServer(local_ip_address, 7777)
receiver = AudioReceiver(local_ip_address, 6666)


# GUI

window = tk.Tk()
window.title("Video Streaming")
window.geometry('300x400')

label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Streaming", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

label_language = tk.Label(window, text="Select Language:")
label_language.pack()

language_var = tk.StringVar()
languages = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Bengali": "bn",
    "Telugu": "te",
    "Marathi": "mr",
    "Tamil": "ta",
    "Urdu": "ur",
    "Punjabi": "pa",
    "Spanish": "es",
    "Gujrati": "gu",

}
language_dropdown = tk.OptionMenu(window, language_var, *languages.keys())
language_dropdown.pack()


translate_button = tk.Button(window, text="Translate", command=translate_text)
translate_button.pack()

window.mainloop()
