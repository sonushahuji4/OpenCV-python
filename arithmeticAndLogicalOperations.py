import cv2
import numpy as np

img1 = cv2.imread('images/3D-Matplotlib.png')
img2 = cv2.imread('images/mainsvmimage.png')

#add = img1 + img2
'''
It is unlikely you will want this sort of messy addition. 
OpenCV has an "add" method, let's see what that does, 
replacing the previous "add" with:
'''
add = cv2.add(img1,img2)
'''
Probably not the ideal here either. We can see that much of the image is very "white." 
This is because colors are 0-255, 
where 255 is "full light." Thus, for example: 
(155,211,79) + (50, 170, 200) = 205, 381, 279...translated to (205, 255,255).
'''

'''
Next, we can add images, and have each carry a 
different "weight" so to speak. 
Here's how that might work:
'''
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/cv2weighted.png',add)