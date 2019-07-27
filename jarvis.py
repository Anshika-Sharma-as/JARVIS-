#%%
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else :
        speak("Good Evening! ")

    speak("I am jarvis sir . Please tell me how may i help you")

#it takes microphone input from user and return the string output.
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anshu.anshikasharma114@gmail.com','8979714667')
    server.sendmail('anshu.anshikasharma114@gmail.com',to, content)
    server.close()



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening..........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try :
        print("Recognizing.......")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said : {query} \n ")

    except Exception as e :
        print(e)
        print("Say that again please....")
        return "None"

    return query




if __name__ == "__main__" :
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for executing task based on the query 
        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(f"According to wikipedia : {results} \n ")
            speak(results)

        elif 'open youtube' in query:
            speak("openning youtube ")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("openning google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("openning stackoverflow ")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak('Openning music')
            music_dir = 'G:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir , the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ANSHIKA SHARMA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak('what should i say ?')
                content = takeCommand()
                to = "233anshika@gmail.com"
                sendEmail(to, content)
                speak('Email has been send ')

            except Exception as e:
                print(e)
                speak('Sorry , sir i am unable to send this email')

        elif 'open notepad' in query:
            speak('Opening notepad')
            notepadPath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(notepadPath)

        elif 'quit' in query:
            print("Quitting...")
            speak("quitting")
            exit()
#%%
