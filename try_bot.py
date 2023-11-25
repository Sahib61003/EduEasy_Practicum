import speech_recognition as sr
import pyttsx3

def load_questions(filename):
    questions = []
    answers = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.strip():
            question, answer = line.split(':')
            questions.append(question.strip())
            answers.append(answer.strip())

    return questions, answers

def initialize_speech_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Select the voice (index 0)
    return engine

def speak(text, engine):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        user_answer = r.recognize_google(audio)
        return user_answer.lower().strip()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

def ask_questions(questions, answers, engine):
    marks = 0
    total_questions = len(questions)

    for i, question in enumerate(questions):
        speak(f"Question {i+1}: {question}", engine)
        user_answer = listen()

        if not user_answer:
            speak("Sorry, I couldn't understand your answer. Please try again.", engine)
            continue

        expected_keywords = answers[i].lower().split()

        user_keywords = user_answer.lower().split()

        unmatched_keywords = [keyword for keyword in expected_keywords if keyword not in user_keywords]
        deduction_percentage = 0.03 * len(unmatched_keywords)
        mark = max(0, 1 - deduction_percentage)

        marks += mark
        print(f"Question: {question}")
        print(f"Expected Answer: {answers[i]}")
        print(f"User Answer: {user_answer}")

        print(f"Mark: {mark}\n")

        marks += mark

    return marks, total_questions

def main():
    filename = 'check.txt'

    questions, answers = load_questions(filename)

    engine = initialize_speech_engine()

    marks, total_questions = ask_questions(questions, answers, engine)
    
    adjusted_marks = marks/total_questions

    percentage = (adjusted_marks / total_questions) * 100

    result_text = f"You obtained {adjusted_marks} marks out of {total_questions}. Your percentage is {percentage:.2f}%."
    speak(result_text, engine)

    print(result_text)



if __name__ == '__main__':
    main()