import cv2
import pytesseract
from google.cloud import translate_v2 as translate
import pyttsx3

# set up Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = r'C:\\Program Files\\Tesseract-OCR\\tessdata'

# set up Google Cloud Translation API
translate_client = translate.Client()

# set up pyttsx3
engine = pyttsx3.init()

# # capture image from camera
# # cap = cv2.VideoCapture(0)
# # ret, frame = cap.read()
# cv2.imwrite("image.jpg", frame)

# # perform OCR on image
# img = cv2.imread('image.jpg')
# text = pytesseract.image_to_string(img, lang='eng', config=tessdata_dir_config)


# Load the input image
img = cv2.imread('aditya.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply image pre-processing techniques, if necessary
# ...

# Convert the image to text using Tesseract OCR
text = pytesseract.image_to_string(gray)

# translate text to Hindi
result = translate_client.translate(text, target_language='hi')
hindi_text = result['input'] + ' -> ' + result['translatedText']

# speak Hindi text
engine.say(hindi_text)
engine.runAndWait()

# release camera and close windows
cap.release()
cv2.destroyAllWindows()
