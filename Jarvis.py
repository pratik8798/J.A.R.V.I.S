from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
from pygame import mixer # Load the required library
import time


#tts=gTTS(text=audio,lang='en')
#tts.save("audio.mp3")


def talkBack(audio):
    print(audio)
    tts=gTTS(text=audio,lang='en')
    tts.save(audio+".mp3")
    mixer.init()
    try:
        music=open('f://PYTHON PROJECTS//J.A.R.V.I.S//'+audio+'.mp3')
        mixer.music.load(music)
        mixer.music.play()
        time.sleep(3)

        mixer.music.stop()
        #print("in")
        music.close()
        '''
            active = pygame.mixer.get_init() 
        if active != None: 
            pygame.mixer.music.stop() 
            pygame.mixer.quit() 
            pygame.quit() 
        if os.path.isfile(my_file): 
            os.remove(my_file) 
        '''
    except IOError:
        print("Couldnt open file")
    


#listens to commands
def myCommand():
    r=sr.Recognizer()
    command="default"
    with sr.Microphone() as source:
        print("Speak now...")
        r.pause_threshhold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    try:
        command=r.recognize_google(audio).lower()
        if "exit" in command:
            talkBack("Thank You Have a Good day ")

            exit()
        print("You said:"+command)
        return command

    
    #loop back to listening to commands if error
    except sr.UnknownValueError:
        #print("Couldn't hear last command :(")
        talkBack("Couldn't hear last command")
        command=myCommand()
    return command
#if else tree for trying out some commands
def assistant(command):
    if "open youtube" in command:
        chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)

        url_path="https://www.youtube.com"
        webbrowser.get('chrome').open_new_tab(url_path)
    elif "open webpage" in command:
        talkBack("Which webpage to open ")
        #time.sleep(2)

        webpage=myCommand()

        chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)

        url_path="https://www."+webpage+".com"
        webbrowser.get('chrome').open_new_tab(url_path)
    elif "google search" in command:
        talkBack("What would you like to search")
        search=myCommand()
        
        url_path = "https://www.google.com.tr/search?q={}".format(search)

        chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
        webbrowser.get('chrome').open_new_tab(url_path)
    elif "what are you doing" in command:
        talkBack("Listening to your commands ")
    elif "how are you" in command:
        talkBack("Fine Thank you")
        talkBack("How are you")
        reply=myCommand()
        if "not" in reply:
            talkBack("Negative reply")
        else:
            talkBack("Positive reply") 
    elif "thank you" in command:
        talkBack("Welcome ")
    elif "email" in command:
        talkBack("Whom to send ")
        #time.sleep(2)

        recipient=myCommand()

        if "john" in recipient:
            talkBack("What should I say")
            content=myCommand()

            mail=smtplib.SMTP("smtp.gmail.com",587)

            #identify server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            mail.login("test1@gmail.com","ur_password")
            mail.sendmail("Test","test@gmail.com",content)

            #close
            mail.close()

            talkBack("Email send")
        else:
            print("Nope")

    elif "exit" in command:
        talkBack("Thank You Have a Good day ")
        exit()        


    else:
        talkBack("I don't know what you mean")
    return
    
talkBack("I am ready for your command ")

while True:

    assistant(myCommand())




