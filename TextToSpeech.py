import pyttsx3
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[1].id)
tts.say('Say anything')
tts.runAndWait()

