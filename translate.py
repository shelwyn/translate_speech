import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

translator = Translator()
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Now:")
    audio = r.listen(source)

trans=['hi','mr','ml','ta'] #List of Language names: https://meta.wikimedia.org/wiki/Template:List_of_language_names_ordered_by_code
for tr in trans:
    print(tr)
    try:
        print("Recognized as: ", r.recognize_google(audio))
        language = tr #change language here
        translations=translator.translate(r.recognize_google(audio), dest=language) #
        print(translations.origin, ' -> ', translations.text)
        myobj = gTTS(text=translations.text, lang=language)
        myobj.save(tr + ".mp3")
        playsound(tr + ".mp3")
    except sr.UnknownValueError:
        print("Audio Error")
    except sr.RequestError as e:
        print("Cloud Error; {0}".format(e))

