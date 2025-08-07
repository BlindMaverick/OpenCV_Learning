import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")
cv.imshow("Blank", blank)

blank[200:300 , 300:400] = 0, 0, 255  # Filling a part of the image with blue color
cv.imshow("Filled Part", blank)

cv.waitKey(0)