import cv2
import numpy as np
from random import randrange

def createImgWithPointRand(h,w):
    img = np.ones((h,w),np.float32)
    randY,randX = randrange(h),randrange(w)
    #print(randY, " ", randX)
    img[randY,randX] = 0
    return img

def determineBlackPixel(img):
    h, w = img.shape
    for y in range(h):
        for x in range(w):
            if img[y,x] == 0:
                return y,x


heightImg, widthImg = 200, 400
img = createImgWithPointRand(heightImg, widthImg)
(py, px) = determineBlackPixel(img)
#print(a, " ", b)
q = 'a'
pas = 3



while(True):
    #bas (2)
    if 50 == q and py+pas < heightImg:
        img[py,px] = 1
        py = py+pas
        img[py,px] = 0
    #haut (8)
    if 56 == q and py-pas > 0:
        img[py,px] = 1
        py = py-pas
        img[py, px] = 0
    #gauche (4)
    if 52 == q and px-pas > 0:
        img[py,px] = 1
        px = px - pas
        img[py, px] = 0
    #droite (6)
    if 54 == q and px+pas < widthImg:
        img[py,px] = 1
        px = px + pas
        img[py, px] = 0

    imgRes = img.copy()
    imgRes[py-5:py+5, px-5:px+5] = 0
    cv2.imshow("Image vide", imgRes)
   
    q = cv2.waitKey(0) & 0xFF
    if ord('0') == q:
    #if q == 48:
        break

cv2.destroyAllWindows()
