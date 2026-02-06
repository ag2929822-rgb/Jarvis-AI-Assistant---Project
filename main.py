import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import time
from openai import OpenAI
from gtts import gTTS
import pygame
import os
# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "dbe4edf12e1a4a11b3003328c3e6db52"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
   
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music finishes
    while pygame.mixer.music.get_busy():
         pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove('temp.mp3')


def aiProcess(command):
    client = OpenAI( api_key ="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")
    
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are virtual assitant name Jarvis skilled general task like alexa and google cloud give short reponse"},
        {"role": "user", "content": command}
    ]
)

    return completion.choices[0].message.content


def processeCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles[:5]:
                speak(article["title"])
    else:
        # Let OpemAi Handle the requests
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Intializing Jarvis....")
    while True:
        r = sr.Recognizer()
        print("recognizing.....")

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = r.listen(source, timeout=7, phrase_time_limit=5)

            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                time.sleep(0.3)
                speak("Ya")

                with sr.Microphone() as source:
                    print("Jarvis Active.....")
                    audio = r.listen(source, timeout=7, phrase_time_limit=6)
                    command = r.recognize_google(audio)
                    processeCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
