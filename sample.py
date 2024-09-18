import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import webbrowser
import datetime


# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and return it as text
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print(f"User said: {command}")
            return command
    except Exception as e:
        print("Error: " + str(e))0
        return ""

# Function to handle the recognized command
def run_voice_assistant():
    command = take_command()

    if 'open google' in command:
        talk('Opening Google')
        webbrowser.open('https://www.google.com')
    elif 'open spotify' in command:
        talk('Opening Spotify')
        webbrowser.open('https://www.spotify.com')
    elif 'open youtube' in command:
        talk('Opening YouTube')
        webbrowser.open('https://www.youtube.com')
    elif 'open twitter' in command:
        talk('Opening Twitter')
        webbrowser.open('https://www.twitter.com')
    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
    elif 'create a reminder' in command:
        talk('What should I remind you about?')
        reminder = take_command()
        with open('reminders.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()}: {reminder}\n")
        talk('Reminder created.')
    elif 'play a song' in command:
        talk('Which song would you like to hear?')
        song = take_command()
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    elif 'open whatsapp' in command:
        talk('Opening WhatsApp')
        webbrowser.open('https://web.whatsapp.com')
    elif 'open my college portal' in command:
        talk('Opening college portal')
        webbrowser.open('https://uni-mysore.ac.in/engineering/')
    else:
        talk('I did not understand the command.')

# Keep the assistant running
while True:
    if run_voice_assistant():
        break

