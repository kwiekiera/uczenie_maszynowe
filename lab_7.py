import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:/Users/kamil/AppData/Local/Tesseract-OCR/tesseract.exe'

def showText(name):
    image = cv2.imread(name)
    print(pytesseract.image_to_string(image))
    print()

showText('pitbull.jpg')
showText('dowod.jpg')
showText('ksiazka.jpg')
showText('teksty.jpg')
showText('smile.jpg')

