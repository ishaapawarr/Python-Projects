import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome To RoboSpeaker 1.1. Created By Isha Pawar")
    speak("Welcome to RoboSpeaker 1.1. Created by Isha Pawar")

    while True:
        speak("Enter what you want to say")

        x = input("Enter what you want to say (or 'q' to quit): ")
        if x.lower() == "q":
            speak("Have a good day!")
            break
        speak(x)