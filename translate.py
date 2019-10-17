import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

translator = Translator()
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Now:")
    audio = r.listen(source)
try:
    #List of Language names: https://meta.wikimedia.org/wiki/Template:List_of_language_names_ordered_by_code
    print("Recognized as: ", r.recognize_google(audio))
    language = "hi" #change language here
    translations=translator.translate(r.recognize_google(audio), dest=language) #
    print(translations.origin, ' -> ', translations.text)
    myobj = gTTS(text=translations.text, lang=language)
    myobj.save("speech.mp3")
    playsound("speech.mp3")
except sr.UnknownValueError:
    print("Audio Error")
except sr.RequestError as e:
    print("Cloud Error; {0}".format(e))
