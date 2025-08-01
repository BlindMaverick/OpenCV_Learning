import cv2 as cv

def rescaleImage(image, scale=0.75):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dimension = (width, height)
    
    return cv.resize(image, dimension, interpolation=cv.INTER_AREA)

image = cv.imread('../Photos/cat_2.jpg')
rescaled_image = rescaleImage(image, scale=0.5)
cv.imshow('Original Cat Image', image)
cv.imshow('Rescaled Cat Image', rescaled_image)

cv.waitKey(0)