import speech_recognition as sr
import os
import pyjokes
import wikipedia
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
from ecapture import ecapture as ec

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
    engine.say("Good Morning!")
    engine.runAndWait()
elif hour>=12 and hour<18:
    engine.say("Good Afternoon!")
    engine.runAndWait()  
else:
    engine.say("Good Evening")
    engine.runAndWait()  
engine.say("I am Friday Sir. Please tell me how may I help you")
engine.runAndWait()

def cmd():
    global text
    text=""
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything..')
        recordedaudio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

    except Exception as ex:
        print(ex)
    if 'chrome' in text or 'google' in text:
        a='Opening google chrome..'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files (x86)\Google\Chrome\Application\Chrome"
        subprocess.Popen([programName])
    elif 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    elif "game" in text or "videogame" in text or "play game" in text:
        engine.say("Hold On a Sec ! Let me start your game")
        engine.runAndWait()
        webbrowser.open('https://poki.com/')
    elif 'play' in text:
        a='opening youtube..'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    elif 'youtube' in text:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
    elif "camera" in text or "take a photo" in text:
            ec.capture(0, "Friday's Camera ", "img.jpg")
    elif 'your name' in text:
        c="Hi, My name is Friday"
        engine.say(c)
        engine.runAndWait()
    elif 'hello' in text or 'hi' in text or 'who are you' in text:
        c="Hi, My name is Friday, how may i help you"
        engine.say(c)
        engine.runAndWait()
    elif 'favourite song' in text or 'favourite music' in text:
        c="my favourite song is GUMMY BEAR. Let me play it for you"
        engine.say(c)
        engine.runAndWait()
        pywhatkit.playonyt("https://www.youtube.com/watch?v=astISOttCQ0")
    elif 'joke' in text:
        j=pyjokes.get_joke()
        print(j)
        engine.say(j)
        engine.runAndWait()       
    elif 'who is' in text:
        try:
            person = text.replace('who is', '')
            info = wikipedia.summary(person, 1)
            engine.say(info)
            print(info)
            engine.runAndWait()
        except:
            idk="""I dont know this person, he may not be famous.
                    But i will try to search it on google"""
            engine.say(idk)
            engine.runAndWait()
            text=text.replace('who is','')
            s=('searching for',text)
            engine.say(s)
            engine.runAndWait()
            pywhatkit.search(text)
    elif 'what is' in text:
        try:
            person = text.replace('what is', '')
            info = wikipedia.summary(person, 1)
            engine.say(info)
            print(info)
            engine.runAndWait()
        except:
            idk="""I dont know what that is, sorry!!.
                But i will try to search it on google"""
            engine.say(idk)
            engine.runAndWait()
            text=text.replace('who is','')
            s=('searching for',text)
            engine.say(s)
            engine.runAndWait()
            pywhatkit.search(text)
    elif 'f***' in text or 'madarchod'in text or 'bhenchod'in text or 'gand' in text or 'chutiya' in text:
        import mf 
        f='Fuck you too, you motherfucking bitch'
        engine.say(f)
        engine.runAndWait()
    elif 'search' in text:
        text=text.replace('search','')
        s=('searching for',text)
        engine.say(s)
        engine.runAndWait()
        pywhatkit.search(text)
    elif "made" in text or "created you" in text or "invented you" in text:
        m=''' i was created by RAJ, he is a very intelligent guy,
he is persuing his computer engineering degree in Thakur college of engineering,
he is currently in third year, division B, roll number 19, give him good marks 
in all exams, or i will kill you in your sleep '''
        engine.say(m)
        engine.runAndWait()
    elif 'powerpoint' in text or 'power point' in text:
        engine.say("opening Power Point presentation 2016")
        engine.runAndWait()
        power = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint 2016"
        os.startfile(power)
    elif 'word' in text or 'microsoft word' in text:
        engine.say("opening microsoft word 2016")
        engine.runAndWait()
        power = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word 2016"
        os.startfile(power)
    elif 'shutdown' in text:
        engine.say("Hold On a Sec ! Your system is on its way to shut down")
        engine.runAndWait()
        subprocess.call('shutdown / p /f')
        exit
    elif "restart" in text:
        engine.say("Hold On a Sec ! Your system is on its way to restart")
        engine.runAndWait()
        subprocess.call(["shutdown", "/r"])
    
        
    
    else:
        engine.say("I can't understand you, please be clear ")
        engine.runAndWait()
    
        
while True:
    cmd()

