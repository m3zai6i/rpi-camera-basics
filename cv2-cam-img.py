import numpy as np
import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

cv2.imwrite('frame.jpg',frame)

# cv2.imshow('frame',frame)

# When everything done, release the capture
cap.release()
