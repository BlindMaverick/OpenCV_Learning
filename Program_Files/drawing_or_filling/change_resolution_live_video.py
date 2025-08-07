import cv2 as cv

def changeResolution(capture, width, height):
    capture.set(cv.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, height)

video = cv.VideoCapture(0)
changeResolution(video, 640, 480)  # Set resolution before capturing

while True:
    isTrue, frame = video.read()
    if not isTrue:
        break

    cv.imshow('Live Video Resized', frame)  # 'frame' is already 640x480 (if camera supports it)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
