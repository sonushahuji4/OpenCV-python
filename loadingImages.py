import cv2
import numpy as np
import matplotlib.pyplot as plt

# video is measured frame per second and each frame is image

'''
---------------Note------------
IMREAD_GRAYSCALE = 0
IMREAD_COLOR = 1
IMREAD_UNCHANGED = -1
'''
'''
There are various way of showing the images like...
1) by matplotlib
2) opencv 
'''
'''
Showing images using OpenCV
'''
img=cv2.imread('images/watch.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img) # To display image data, use the imshow function
cv2.waitKey(0)  # Waits for a pressed key
cv2.destroyAllWindows() # The function destroyAllWindows destroys all of the opened HighGUI windows
cv2.imwrite('saveImages/watch.png',img) # Saves an image to a specified file