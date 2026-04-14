import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" NOt Understanding ")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice' , voices[0].id)     #0-male 1- female
    rate = engine.getProperty('rate')
    engine.setProperty('rate',175)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    # if sptext().lower() == "hello":
    while True :
        data1 = sptext().lower()

        if  "your name" in data1:
            name = "my name is arjun"
            speechtx(name)

        elif "old are you" in data1:
            age = " i am 20 years old"
            speechtx(age)

        elif 'time' in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)

        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/watch?v=N-iO1tDmP1A&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=5")

        elif "joke" in data1:
            joke_1 = pyjokes.get_jokes(language="en" , category="neutral")
            print(joke_1)
            speechtx(joke_1)

        elif 'song' in data1:
            add = "D:\SON"
            listsong = os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add,listsong[24]))

        elif "exit" in data1:
            speechtx("thank you")
            break

        time.sleep(5)
    # else:
    #     print("thanks")


