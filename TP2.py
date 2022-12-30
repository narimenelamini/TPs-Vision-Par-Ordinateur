import cv2
import numpy as np 
import matplotlib.pyplot as plt
img =cv2.imread("visible.jpg",cv2.IMREAD_GRAYSCALE)
if img is None :
    print('erreur de chargement')
    exit(0)
img[:,:] = img[:,:] /2
min = 255 
max = 0
h,w =img.shape
#img_YCrCb = cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
for y in range(h):
    for x in range(w):
        if img[y,x] < min :
            min = img[y,x]
        if img[y,x] > max:
            max = img[y,x]
imgRes=np.zeros(img.shape,img.dtype)

hist_avant = np.zeros((256,1),np.uint16) #tableau vide de 256 cases
hist_apres = np.zeros((256,1),np.uint16)
for y in range(h) :
  for x in range(w) :
    imgRes[y,x]= (img[y,x] - min)*255/ (max-min) 
    hist_avant[img[y,x],0]+=1 #incrémenter le niveau de gris selon notre image

hist_apres = cv2.calcHist([imgRes],[0],None,[256],[0,255])



plt.figure()
plt.title("image normalisé")
plt.xlabel("NG")
plt.ylabel("NB")
plt.plot(hist_avant)
plt.plot(hist_apres)
plt.xlim([0,255])
plt.show()




#cv2.imshow('img avant normalisation',img)
#cv2.imshow('img aprés normalisation',imgRes)
cv2.waitKey(0)
cv2.destroyAllWindows