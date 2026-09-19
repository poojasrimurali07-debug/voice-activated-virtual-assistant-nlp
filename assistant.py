import speech_recognition as sr
import pyttsx3
from datetime import datetime


# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    """Convert text response into speech."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Capture voice input and convert it into text."""
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I could not understand what you said.")
            return ""

        except sr.RequestError:
            speak("Sorry, the speech recognition service is unavailable.")
            return ""


def process_command(command):
    """Analyze the command and decide the appropriate response."""

    if "hello" in command or "hi" in command:
        return "Hello! How can I help you?"

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in command:
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}."

    elif "your name" in command:
        return "I am a voice activated virtual assistant."

    elif "how are you" in command:
        return "I am doing well. Thank you for asking."

    elif "exit" in command or "stop" in command or "bye" in command:
        return "Goodbye! Have a great day."

    else:
        return "I understood your command, but I do not have an action for it yet."


def main():
    """Main application loop."""
    speak("Hello! I am your voice activated virtual assistant.")

    while True:
        command = listen()

        if not command:
            continue

        response = process_command(command)
        speak(response)

        if "exit" in command or "stop" in command or "bye" in command:
            break


if __name__ == "__main__":
    main()