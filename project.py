import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

import cv2

img = cv2.imread('img5.jpg')
cv2.imshow('sample img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

text = pytesseract.image_to_string(img)
print(text) 

import pyttsx3

text_speech = pyttsx3.init()
text_speech.say(text)
text_speech.runAndWait()