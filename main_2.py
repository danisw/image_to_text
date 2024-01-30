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


print("reading threshold")
#tresholding is a method in image processing to separate background with object, using tresh binary because anything below treashold will be chosen as black
ret, image = cv.threshold(initial_image, 98, 255, cv.THRESH_BINARY)
cv.imshow('', image)
cv.waitKey(0)

print("reading border image")
results = pytesseract.image_to_data(image, output_type=Output.DICT, config="--psm 6")
for i in range(0, len(results["text"])):
    # extract the bounding box coordinates of the text region from
    # the current result
    x = results["left"][i]
    y = results["top"][i]
    w = results["width"][i]
    h = results["height"][i]
    # extract the OCR text itself along with the confidence of the
    # text localization
    text = results["text"][i]
    conf = float(results["conf"][i])

    # filter out weak confidence text localizations
    if conf > 10:

        # strip out non-ASCII text, so we can draw the text on the image
        # using OpenCV, then draw a bounding box around the text along
        # with the text itself
        cv.rectangle(unchanged_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(img=unchanged_image, text=text, org=(x, y), fontFace=cv.FONT_HERSHEY_COMPLEX,
                   fontScale=0.3, color=(36, 0, 255), thickness=1)

cv.imshow('', unchanged_image)
cv.waitKey(0)


