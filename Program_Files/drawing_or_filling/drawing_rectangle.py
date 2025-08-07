import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")

# Drawing a rectangle
cv.rectangle(blank, (1, 1), (250, 250), (0, 255, 0), thickness=2)
cv.imshow("Rectangle", blank)


# Drawing a filled rectangle
cv.rectangle(
    blank, (1, 1), (400, 400), (0, 255, 0), thickness=cv.FILLED
)  # alternative: thickness=-1
cv.imshow("Filled Rectangle", blank)

cv.waitKey(0)
