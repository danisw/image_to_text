import cv2 as cv
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from pytesseract import Output
from fuzzywuzzy import fuzz

print("reading initial image")
#get image as it is
unchanged_image = cv.imread("toefl.jpeg", cv.IMREAD_UNCHANGED)
#change to grayscale
initial_image = cv.imread("toefl.jpeg", 0)
cv.imshow('', initial_image)
cv.waitKey(0)

print("grayscaling image")
# Grayscale, Gaussian blur, Otsu's threshold
image = cv.imread('toefl.jpeg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (3,3), 0)
thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
cv.imshow('thresh', thresh)
cv.waitKey(0)

print("remove noise")
# Morph open to remove noise and invert image
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)
cv.imshow('opening', opening)
cv.waitKey(0)

print("inverting")
#inverting
invert = 255 - opening
cv.imshow('invert', invert)
cv.waitKey(0)

# Perform text extraction
data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
print(data)
