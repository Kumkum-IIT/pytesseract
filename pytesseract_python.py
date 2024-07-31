import cv2
import numpy as np
import pytesseract
import re

image = cv2.imread('image.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

gray = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

kernel = np.ones((2,2), np.uint8)
thresh = cv2.dilate(thresh, kernel, iterations=1)
thresh = cv2.erode(thresh, kernel, iterations=1)

thresh = cv2.bitwise_not(thresh)

custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ '

data = pytesseract.image_to_string(thresh, lang='eng', config=custom_config)

def process_line(line):
    # Remove spaces between letters
    line = re.sub(r'\s+', '', line)
    # Add spaces between words (before capital letters, except at the start)
    line = re.sub(r'(?<!^)(?=[A-Z])', ' ', line)
    return line

lines = data.split('\n')
processed_lines = []
for line in lines:
    if line.strip():  # Remove empty lines
        processed_line = process_line(line.strip())
        processed_lines.append(processed_line)

# if "THIS" not in processed_lines[0] and len(processed_lines) > 1:
#     processed_lines[0] += " THIS"

result = '\n'.join(processed_lines)

print(result)

