from gtts import gTTS
import os

text1='hi how are you'
language='en'
obj=gTTS(text=text1,lang=language,slow=False)
obj.save('testaudio.mp3')
os.system('testaudio.mp3')