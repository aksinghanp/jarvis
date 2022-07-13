from datetime import datetime
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
# provide voice by window
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis sir. Plzz  tell how may I help u")

def takeCommand():
    '''
     it takes microphone command from the user and return string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    
    except Exception as e:
        print(e)
        print("say that again...")
        return "None"
    return query    

if __name__=="__main__":
    # speak("harry is a good boy")   
    # wishMe() 
    # while True:
    if 1:    
      query=takeCommand().lower()

    #logic to execute tasks based on query
      if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        speak(results)

      elif 'open youtube' in query:
        webbrowser.open("youtube.com")

      elif 'open google' in query:
        webbrowser.open("google.com")
         
      elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

      elif 'play music' in query:
        music_dir='filepath in pc '
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path(music_dir,songs[0]))

      elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")   
          
 