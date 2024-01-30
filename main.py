import numpy as np
import cv2

cap = cv2.VideoCapture("videos/20240123_103912_Malika_beach.mp4")

fgbg = cv2.createBackgroundSubtractorMOG2()

# https://www.geeksforgeeks.org/python-opencv-background-subtraction/
# https://docs.opencv.org/4.9.0/d1/dc5/tutorial_background_subtraction.html
while 1:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow("frame", fgmask)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
