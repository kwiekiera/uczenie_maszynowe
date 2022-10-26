import pytesseract
import cv2

def showText(name):
    image = cv2.imread(name)
    print(pytesseract.image_to_string(image))
    print()

showText('pitbull.jpg')
showText('dowod.jpg')
showText('ksiazka.jpg')
showText('teksty.jpg')
showText('smile.jpg')

