import cv2 as cv
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

video = cv.VideoCapture('../Videos/dog_video.mp4')

while True:
    isTrue, frame = video.read()

    frame_resized = rescaleFrame(frame, scale=0.2)
    
    cv.imshow('Dog Video', frame)
    cv.imshow('Rescaled Dog Video', frame_resized)
    
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
