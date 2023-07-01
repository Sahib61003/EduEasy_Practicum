import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

    try:
        #using Google Speech Recognition
        text = r.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    except sr.RequestError as e:
        print("Error occurred during speech recognition:", str(e))
