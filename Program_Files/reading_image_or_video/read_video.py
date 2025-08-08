import cv2 as cv

video = cv.VideoCapture('../Videos/dog_video.mp4')

while True:
    isTrue, frame = video.read()

    cv.imshow('Dog Video', frame)
    
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
