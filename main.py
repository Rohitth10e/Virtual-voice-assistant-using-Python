import os
import subprocess
import sys
import pyttsx3 as tts
import pytz
import pywhatkit as kit
import datetime
import openai
import speech_recognition as sr
import win32com.client
import webbrowser
from config import apikey
import random

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Rohith: {query}\nTars: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = '''Your api key'''
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)
        say(f"{prompt} finished")



speaker=win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    speaker.Speak(text)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1;
        audio=r.listen(source)
        try:
            # print("recognizing")
            query=r.recognize_google(audio,language="en-in")
            print("User said {0}".format(query))
            return query
        except Exception as e:
            return "Please try again"

say("Hey I am A I assistant. how can i help you?")
while True:
    print("Listening...")
    query = takeCommand().lower()
    sites=[["youtube","https://youtube.com"],["wikipedia","https://wikipedia.org"],["google","https://google.com"]]
    for site in sites:
        if "Open {0}".format(site[0]).lower() in query.lower():
            say("Opening{0}".format(site[0]))
            webbrowser.open(site[1])

    if "play music".lower() in query.lower():
        musicPath = "D:\Music"
        songs=os.listdir(musicPath)
        os.startfile(os.path.join(musicPath,songs[0]))
        # os.system(f"open {musicPath}")

    elif "what is the time" in query:
        india_timezone = pytz.timezone('Asia/Kolkata')
        utc_now = datetime.utcnow()
        localized_time = utc_now.replace(tzinfo=pytz.utc).astimezone(india_timezone)
        formatted_time = localized_time.strftime('%Y-%m-%d %H:%M:%S %Z')
        # hour = datetime.datetime.now().strftime("%H")
        # min = datetime.datetime.now().strftime("%M")
        # amPm=datetime.datetime.now().strftime("%p")
        # say(f"The time is {hour} {min} {amPm}")
        say(f"Localized time in Karntaka: {formatted_time}")

    elif "open vs Code".lower() in query.lower():
        say("Opening Vs Code")
        codePath="D:/Microsoft VS Code/Code.exe"
        os.startfile(codePath)

    elif "Using artificial intelligence".lower() in query.lower():
        ai(prompt=query)

    elif "Quit".lower() in query.lower():
        say("Turning off")
        exit()

    elif "reset chat".lower() in query.lower():
        chatStr = ""

    elif "Cosmo Introduce yourself".lower() in query.lower():
        say("Hey there I'm Cosmo your virtual voice assistant prepared and presented by Shabhaaz and Rohith of 3rd year BE CSE students I'm here to assist you with information, answer your questions, or just engage in a friendly conversation. Feel free to ask me anything or let me know how I can help you today. ")

    else:
        print("Chatting...")
        chat(query)


# say("Hey how are you?")

