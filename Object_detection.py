import os

import cv2


img = cv2.imread(os.path.join('.', '2_dogs.jpeg'))
cv2.imshow('img', img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


edge_detection=cv2.Canny(img, 100, 200)
cv2.imshow('edge_detection', edge_detection)


ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
white_image=cv2.imread(os.path.join('.', 'white_templet.PNG'))

for cnt in contours:
    if cv2.contourArea(cnt) > 200:
     cv2.drawContours(white_image, cnt, -1, (0, 255, 0), 1)

     x1, y1, w, h = cv2.boundingRect(cnt)

     cv2.rectangle(white_image, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
cv2.imshow('white_image', white_image)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()