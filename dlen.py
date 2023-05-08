import cv2
import pytesseract
import pyttsx3
from googletrans import Translator

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Initialize the translator object
translator = Translator()

# Load the image
img = cv2.imread('aditya.png')

# Display the image
cv2.imshow('sample img', img)
# cv2.waitKey(0)
cv2.destroyAllWindows()

# Perform OCR on the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)

# Translate the text from English to Hindi
# translated_text = translator.translate(text, src='en', dest='hi').text
translated_text = translator.translate(text, src='en', dest='hi').pronunciation

# Print the translated text
print(translated_text)

# Initialize the text-to-speech engine
text_speech = pyttsx3.init()

# Set the voice for Hindi
# text_speech.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_HI-IN_HEMANT_11.0')
# voices = text_speech.getProperty('voices')
# for voice in voices:
#     print(voice.id)
# Speak the translated text in Hindi
# text_speech.setProperty('voice', 'com.apple.speech.synthesis.voice.sin-ji')
# text_speech.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\S
# 
# peech\Voices\Tokens\MSTTS_V110_hiIN_Hemant')
# text_speech.setProperty('voice', 'hi')
# Set the speaking rate (higher value = faster speech)
text_speech.setProperty('rate', 180)

# Set the volume (0-1)
# text_speech.setProperty('volume', 1)
text_speech.say(translated_text)
text_speech.runAndWait()
