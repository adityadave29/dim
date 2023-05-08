import pytesseract
import cv2
from googletrans import Translator
import pyttsx3
from gtts import gTTS
from playsound import playsound

# Set the path to Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Create a Translator object
translator = Translator(service_urls=['translate.google.com'])

# Load the input image
img = cv2.imread('aditya.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply image pre-processing techniques, if necessary
# ...

# Convert the image to text using Tesseract OCR
text = pytesseract.image_to_string(gray)

# Print the extracted text
print("Extracted Text:\n", text)

# Translate the text to Hindi
translation = translator.translate(text, dest='hi')

# Print the translated text
print("Translated Text:\n", translation.text)

# Convert the translated text to speech in Hindi
text_speech = pyttsx3.init()
text_speech.setProperty('rate', 150)  # Set the speaking rate (words per minute)
text_speech.setProperty('voice', 'hi')  # Set the voice to Hindi
text_speech.say(translation.text)
text_speech.runAndWait()

# Save the converted audio file in mp3 format
language = "hi"  # Set the language to Hindi
tts = gTTS(text=translation.text, lang=language)
tts.save("output_speech.mp3")

import os
os.startfile("output_speech.mp3")

# Play the converted audio file
# playsound("output_speech.mp3")

