import cv2 as cv

img = cv.imread('../Photos/cat_1.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)

