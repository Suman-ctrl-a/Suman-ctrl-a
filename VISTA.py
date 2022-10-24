import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import subprocess as app
import pywhatkit as wiki 
import smtplib as mail
import os
import webbrowser as net
from functions import greet,hear,speak
greet()
now = datetime.datetime.today()
while True:
    print('What do you want me to do boss?')
    command = hear().lower()
    if 'time' in command:
        speak(now.strftime('The time is %H %M: sir '))
    elif 'WhatsApp message' in command:
        speak('Tell me the recipients phone number boss...')
        phnum = input("Type the recipient's phone number boss...")
        speak('What should i send boss...?')
        print('What should i send boss?')
        message = hear()
        wiki.sendwhatmsg('+91{}'.format(phnum),'{}'.format(message),now.hour,now.minute+2)
        speak('Message sent to {}'.format(phnum))
    elif 'email' in command:
        speak('type me the recipients email-id boss')
        emailid = input("Enter email id ")
        speak('tell me the content boss')
        content = hear()
        server = mail.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('pythonvista@gmail.com','afmdozbfoakzhyfo')
        server.sendmail('pythonvista@gmail.com',
                             '{}'.format(emailid),
                            '{}'.format(content))
        speak('Email send to {}'.format(emailid))
    elif 'know about' in command:
        speak('Searching Wikipedia...')
        query = command.replace("i want to know about", "")
        results = wikipedia.summary(query, sentences=5)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'quit' in command:
        quit()
    elif 'open youtube' or 'open yt' in command:
        net.open("youtube.com")
    else:
        print("Sorry couldn't get you")