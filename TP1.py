import cv2
import numpy as np 
img=cv2.imread("Abdelatif.jpg",cv2.IMREAD_GRAYSCALE)
if img is None :
    print('image is empty')
    exit(0)
h,w=img.shape
##imgresultat=np.zeros((h,w),np.uint8)
imgresultat=np.zeros(img.shape,img.dtype)
## le changement des couleurs (inverse)

for y in range(h) :
  for x in range(w) :
    imgresultat[y,x]=255-img[y,x] ## degradation de noire et blanc (x+y)*255/(h+h)

imgresultat[50:1000,50:200]=0

cv2.imshow('image1',img)
cv2.imshow('image2',imgresultat)
cv2.waitKey(0)
cv2.destroyAllWindows