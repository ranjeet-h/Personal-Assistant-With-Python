import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
"""Voices[0] = for mens voice and voices[1] for girl's voice"""
engine.setProperty('voices', voices[1].id)



def speak(audio):
    '''speak def for speaking. '''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''Wish on thw basis of what time is.'''
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good Morning Boss.")
    elif  hour >= 12 and hour < 18:
        speak("Good Afternoon.")
    elif hour >= 18 and hour < 20:
        speak("Good Evening.")
    else:
        speak("Good Night.")
        
    speak("How you doing so far without me. Do you need help.")


def takeCommand():
    """It takes Microphone input from the user and returning string output"""
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening.....")
        r.energy_threshold = 4000
        r.dynamic_energy_threshold
        r.pause_threshold =  0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #we passed the what we audio we have recived form input to google engine.
        print(f"User said: {query}")

    except Exception as e:
        #print(e)
        print("Say that again please.")
        return "None"
    return query

def sendEmail(to, content):
    '''
    You have to change settings of your account to use this services Read Instructions file.
    go to this link https://myaccount.google.com/u/0/security?hl=en and Turn on Less secure app access.
    
    '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YourEmailID@fgamil.com', 'your password') #Add your email and password
    server.sendmail('YourFriendsEamilId', to, content)
    server.close()

if __name__ == "__main__":
    speak("Hey Boss.")
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower() #we need to convert it because google engine process in lower case.
        
        #  logic for executing tasks based on query.
        if 'wikipedia' in query:
            '''Added wikipedia command to our personal assistant.'''
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia.")
            print(results)
            speak(results)
        
        
        elif 'open youtube' in query:
            '''Added commands to open web pages.'''
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")



        elif 'play music' in query:
            '''specify your own music directory.'''
            Fev_music = 'C:\\Users\\Rohini\\Desktop\\Fev Music' #it works like \n or it skips \ meaning in python interpreter.
            songs = os.listdir(Fev_music)
            print(songs)
            #use random method if you want to suffel through songs.
            os.startfile(os.path.join(Fev_music, songs[1]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Bose, the time is {strTime}")

        elif 'open notepad' in query:
            '''Opening apps by command.'''
            noPad = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(noPad)


        elif 'email to ranjeet' in query:
            #Use dictionary to store emailId and send emails.
            #sorry, not working but i am modifying algorithm's.
            '''Sending email using command.'''
            try:
                speak("What should i say")
                content = takeCommand()
                to = "yourfriendsemail@gmail.com"
                sendEmail(to, content)
                speak("Email has been send.")

            except Exception as e:
                print(e)
                speak("Sorry bose, I am not able to send emails.")




            