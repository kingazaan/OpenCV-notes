import cv2 as cv
import os

# set current working director

os.chdir(r"Users\ab\Documents\GitHub\OpenCV-notes")

# images

window_name = 'Cat'
img = cv.imread(r"Resources/Photos/cat.jpg")

cv.imshow(window_name, img)
cv.setWindowProperty(window_name, cv.WND_PROP_TOPMOST, 1) # openCV settings and configurations

cv.waitKey(0)
cv.destroyAllWindows()

# videos

window_name = 'Video'
capture = cv.VideoCapture(r"Resources/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow(window_name, frame)
    cv.setWindowProperty(window_name, cv.WND_PROP_TOPMOST, 1)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release
cv.destroyAllWindows()

