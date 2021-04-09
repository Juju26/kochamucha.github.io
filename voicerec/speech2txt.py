import speech_recognition as sr
import pyttsx3 
from gtts import gTTS
import os
r=sr.Recognizer()
s='Hi'

def speakcmd(command):
    eng=pyttsx3.init()
    eng.say(command)
    eng.runAndWait()
    print(command) 

def savecmd(com):
    eng=pyttsx3.init()
    eng.say(com)
    eng.runAndWait()
    print('listening  NAME.......')
    audio2=r.listen(source2)

    mytext3=r.recognize_google(audio2)
    mytext2=mytext3.lower()
            
    dir=str(mytext2)
    pare="C:/Users/USER/Desktop/juju/smrt goggles/codes/voicerec/"
    path=os.path.join(pare,dir)
    os.mkdir(path)
    print("Directory '% s' created" %dir)
    #print(com)



print('Hi..')



while(True):
   
    try:
        
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2,duration=0.5)
            print('listening.......')
            audio2=r.listen(source2)

            mytext=r.recognize_google(audio2)
            mytext1=mytext.lower()
            

            if(mytext=='stop'):
                break

            elif (mytext=='save name' or mytext=='save' or mytext=='save save'):
                p='say his name to save'
                speakcmd(p)
                savecmd(p)
                
            speakcmd(mytext1)
            #text2speech(mytext1)
    except sr.RequestError as e:
        ass0='Pardon! Couldnt hear you properly'
    except sr.UnknownValueError:
        ass1='Feel free to command!'
        #print(ass1)
        speakcmd(ass1)
print('stopped')