import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

import smtplib
# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()
def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishMe():
      hour = int(datetime.datetime.now().hour)
      if hour >=0 and hour <12:
          speak("good morning!")
             
      elif hour>=12 and hour<18:
          speak("good afternoon!")
         
      else:
          speak("good evening!")
          
      speak("i am damon how may i help you")  
      
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("user said : {query}\n")
        
    except Exception as e:
        print(e)   
        print("Say that again please...")
        return "None"
    return query

            
def sendEmail(to,content) :
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mail@gmail.com','password')
    server.sendmail('mail@gmail.com',to,content)
    server.close()          
    
if __name__== "__main__":
  wishMe()
  while True:
   query = takeCommand().lower()
 
   if 'wikipedia' in query:
       speak('Searching wikipedia...')
       query = query.replace("wikipedia","")
       results = wikipedia.summary(query, sentences=2)
       speak("according to wikipedia")
       print(results)
       speak(results)
       
   elif'open Youtube' in query:
      webbrowser.open("youtube.com")
    
   elif'open Google' in query:
      webbrowser.open("google.com")
      
   elif'open Stackoverflow' in query:
      webbrowser.open("stackoverflow.com")
   elif'the time' in query:
      strTime= datetime.datetime.now().strftime("%H:%M:%S")
      speak("mam ,the time is {strTime}")
   elif'send email' in query :
       try:
           speak("what should i say") 
           content = takeCommand()
           to = "mail@gmail.com"
           sendEmail(to,content)
           speak("email has been sent")
   
       except Exception as e:
           print(e)
           speak("sorry! my friend mansi i am not able to send mail ")
      
         
       
      