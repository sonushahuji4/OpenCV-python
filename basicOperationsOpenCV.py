import numpy as np
import cv2

img=cv2.imread('images/watch.png',cv2.IMREAD_COLOR)
#print(img)
#px=img[100,100]
img[100,100]=[255,255,255]
img[200:250,200:250]=[255,255,255]
print('img.shape:',img.shape)
print('img.size:',img.size)
print('img.dtype:',img.dtype)
watch_face = img[50:150,100:200]
img[0:100,0:100] = watch_face
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/basicoperationonimage.png',img)
# px=img[100,100]
# print(px)
# ROI => Region of Image (sub image of image)

'''
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,0,0])
    upper_red = np.array([255,255,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    # k = cv2.waitKey(5) & 0xFF
    # if k == 27:
    #     break
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
colorFilteringOpenCV

'''