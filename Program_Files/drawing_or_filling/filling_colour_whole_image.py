import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("Blank", blank)

# Fill the image with blue color
blank[:] = 255, 0, 0
cv.imshow("Blue", blank)


# Fill the image with green color
blank[:] = 0, 255, 0
cv.imshow("green", blank)


# Fill the image with red color
blank[:] = 0, 0, 255
cv.imshow("red", blank)

cv.waitKey(0)