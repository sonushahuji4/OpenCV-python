import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
---------------Note------------
IMREAD_GRAYSCALE = 0
IMREAD_COLOR = 1
IMREAD_UNCHANGED = -1
'''
img=cv2.imread('images/watch.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.show()
cv2.imwrite('saveImages/watch1.jpg',img)