import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Standard Video Dimensions Sizes
STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

width, height = STD_DIMENSIONS["720p"]

cap.set(3, width)
cap.set(4, height)

ret, frame = cap.read()

cv2.imwrite('frame.jpg',frame)

# cv2.imshow('frame',frame)

# When everything done, release the capture
cap.release()
