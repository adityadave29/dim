import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

import cv2

from googletrans import Translator

# Create a Translator object
translator = Translator(service_urls=['translate.google.com'])


# Translate to Hindi

# Print the translated text



img = cv2.imread('aditya.png')
cv2.imshow('sample img',img)
# cv2.waitKey(0)
cv2.destroyAllWindows()

text = pytesseract.image_to_string(img)
print(text) 

translation = translator.translate(text, dest='hi')

import pyttsx3

print()

text_speech = pyttsx3.init()
# text_speech.say(translation)
text_speech.runAndWait()

from gtts import gTTS
from playsound import playsound

# Hindi text to be converted to speech

# Language in which you want to convert the text (in this case, Hindi)
language = "hi"

# Passing the text and language to the gTTS module
tts = gTTS(text=translation.text, lang=language)

# Saving the converted audio file in mp3 format
tts.save("C:/Users/91931/Desktop/DIM/speech.mp3")

# Playing the converted audio file
playsound("C:/Users/91931/Desktop/DIM/speech.mp3")
