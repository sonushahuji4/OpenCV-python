import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    cv2.imshow('frame',frame)   # this is color frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()   # Closes video file or capturing device
cv2.destroyAllWindows()