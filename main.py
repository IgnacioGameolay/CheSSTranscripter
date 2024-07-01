import cv2
import numpy as np
import pytesseract
from filter_img import *

#fixing path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#Functions#
def apply_image_processing(image):
    # Convertir la imagen a escala de grises
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Corrección Gamma
    gamma = 1.5
    imgGamma = np.uint8(np.power(imgGray / float(np.max(imgGray)), gamma) * 255.0)

    # Suavizado Gaussiano
    delta = 5
    kernel_size = (5, 5)
    imgBlur = cv2.GaussianBlur(imgGamma, kernel_size, delta)

    # Umbralización Otsu
    _, th = cv2.threshold(imgBlur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Detección de bordes (Canny)
    imgEdge = cv2.Canny(th, 50, 120)

    return imgEdge  # Devuelve la imagen con bordes detectados




#Main#
path_image = cv2.imread("img.jpg")
img = apply_image_processing(path_image)

text = pytesseract.image_to_string(img, lang='spa')
print("Text: ", text)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()