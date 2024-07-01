import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

img = cv2.imread("img.jpg")

text = pytesseract.image_to_string(img, lang='spa')
print("Text: ", text)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()