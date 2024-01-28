
import numpy as np 
import cv2 

cap = cv2.VideoCapture('videos/20240123_103912_Malika_beach.mp4') 

fgbg = cv2.createBackgroundSubtractorMOG2() 

while(1): 
	ret, frame = cap.read() 

	# applying on each frame 
	fgmask = fgbg.apply(frame) 

	cv2.imshow('frame', fgmask) 
	k = cv2.waitKey(30) & 0xff
	if k == 27: 
		break

cap.release() 
cv2.destroyAllWindows() 

