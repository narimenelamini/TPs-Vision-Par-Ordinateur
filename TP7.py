import cv2
import numpy as np 
img =cv2.imread("images.jpg",cv2.IMREAD_COLOR)
if img is None :
    print('erreur de chargement')
    exit(0)
#1. Récupération des couleurs d'une image
img_b = np.zeros(img.shape,img.dtype)
img_g = np.zeros(img.shape,img.dtype) #  img_b.copy()
img_r = np.zeros(img.shape,img.dtype)  #  img_b.copy()
img_gray = (img[:,:,0] + img[:,:,1] + img[:,:,2])/3
#récupérer la couleur bleu de l'image
#bleu : 0 (qu'on veut récupérer)
#red : 1
# green : 2
img_b[:,:,0] = img[:,:,0]
img_g[:,:,1] = img[:,:,1]
img_r[:,:,2] = img[:,:,2]

#2.Convertir l'image  en HSV
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_YCbCr = cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
#3. Convertir le type de l image to 16 bits type
img_16bits = np.uint16(img) *255 # cette fct tient à changer seulement le type . pour afficher l image correvtement on doit multiplier* 255
img_32float = np.float32(img) /255 # pour avoir l'intervalle [0,1]
cv2.imshow('img BGR',img)
cv2.imshow('img img_YCbCr',img_YCbCr)
#cv2.imshow('img 32FLOAT',img_32float)
#cv2.imshow('img HSV',img_rgb)
#cv2.imshow('img HSV',img_hsv)
#cv2.imshow('img_16',img_16bits)
#cv2.imshow('img G',img_g)
#cv2.imshow('img R',img_r)
#cv2.imshow('img B',img_b)
cv2.waitKey(0)
cv2.destroyAllWindows
#imshow supports images 8bits (255)/16bit (16^2 - 1) / float entre 0 et 1, else: error