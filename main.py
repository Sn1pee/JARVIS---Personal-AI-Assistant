import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# This code implements a simple voice assistant named Jarvis that listens for the wake word "Jarvis"
# and responds to various commands such as opening websites, playing music, and fetching news.

# Imported and installed libraries:
# speech_recognition: For recognizing speech from the microphone.
# pip install pocketsphinx
# webbrowser: For opening URLs in the web browser.
# pyttsx3: For text-to-speech conversion.
# Note: Make sure to install the required libraries using pip before running this code.
# This is a simple voice assistant named Jarvis that listens for the wake word "Jarvis"

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = os.getenv("NEWS_API")


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('hello.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('hello.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("hello.mp3")

def aiProcess(command):
    token = os.environ["GITHUB_TOKEN"]
    endpoint = "https://models.github.ai/inference"
    model = "openai/gpt-4.1"

    client = OpenAI(
        base_url=endpoint,
        api_key=token,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud",
            },
            {
                "role": "user",
                "content": command,
            }
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )

    return response.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")  
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "opne linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles from the response
            articles = data.get('articles', [])
            
            # Print the titles of the articles
            for article in articles:
                speak(article['title'])
    
    else:
        # Let OpenAI handle the command
        output = aiProcess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    # Listen for the wake work Jarvis
    # obtain audio from the microphone
    while True:
        r = sr.Recognizer()
    
        # recognize speech using google
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Ya")
                #listen for the command after the wake word
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
