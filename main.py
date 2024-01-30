from PIL import Image 
import pytesseract
import numpy as np 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


#simple and clean image
filename = 'iamge_01.jpg'
img_1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img_1)
print(text)

#image with noise background
filename = 'blur_image.jpg'
img_2 = np.array(Image.open(filename))
norm_img = np.zeros((img_2.shape[0], img_2.shape[1]))
img = cv2.normalize(img_2, norm_img, 0, 255, cv2.NORM_MINMAX)
img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
img = cv2.GaussianBlur(img, (1, 1), 0)
text = pytesseract.image_to_string(img)
print(text)

#image with complex text
filename = 'toefl.jpeg'
img_3 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img_3)
print(text)

#given text 
gt = "Paramita Daniswari public 2018"

#calculate the similarity
print(f"Token sort ratio similarity score: {fuzz.partial_ratio(text, gt)}")
print(f"Token sort ratio similarity score: {fuzz.token_sort_ratio(text, gt)}")
#fuzz.partial_ratio(text, gt)
