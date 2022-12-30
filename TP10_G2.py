import cv2
import numpy as np
from KalmanFilter import KalmanFilter

lo=np.array([95, 80, 60])
hi=np.array([115, 255, 150])
def detect_inrange(image, surfaceMin,surfaceMax):
    points=[]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image=cv2.blur(image, (5, 5))
    mask=cv2.inRange(image, lo, hi)
    mask=cv2.erode(mask, None, iterations=2)
    mask=cv2.dilate(mask, None, iterations=2)
    elements=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    elements=sorted(elements, key=lambda x:cv2.contourArea(x), reverse=True)
    for element in elements:
        print('surface  :',cv2.contourArea(element))
        if cv2.contourArea(element)>surfaceMin and cv2.contourArea(element)<surfaceMax:
            ((x, y), rayon)=cv2.minEnclosingCircle(element)
            points.append(np.array([int(x), int(y),int(rayon),int(cv2.contourArea(element))]))

    return image, mask, points

def detect_visage(image):
    face_cascade=cv2.CascadeClassifier("./haarcascade_frontalface_alt2.xml")
    points=[]
    rects=[]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
    for x, y, w, h in face:
        points.append(np.array([int(x+w/2), int(y+h/2)]))
        rects.append(np.array([(x, y),(x+w, y+h)]))
    return points, rects

VideoCap=cv2.VideoCapture(0)
KF=KalmanFilter(0.1, [0,0])

while(True):
    mask=None
    rects=None
    ret, frame=VideoCap.read()
    cv2.flip(frame,1,frame)
    etat=KF.predict().astype(np.int32)
    #points, mask = detect_inrange(frame,1000,5000)
    points, rects = detect_visage(frame)
    cv2.circle(frame, (int(etat[0]), int(etat[1])), 2, (0,255,0), 5)
    cv2.arrowedLine(frame,(int(etat[0]), int(etat[1])), (int(etat[0]+etat[2]), int(etat[1]+etat[3])), color=(0,255,0), thickness=3, tipLength=0.2)

    cv2.circle(frame, (100, 100), 20, (0, 255, 0), 5)
    #print(image[100,100])
    if (len(points)>0):
        cv2.circle(frame, (points[0][0], points[0][1]), 10, (0, 0, 255), 2)
        KF.update(np.expand_dims(points[0], axis=-1))
        
    if rects is not None:
        try:
            cv2.rectangle(frame, rects[0][0], rects[0][1], (0,0,255),1,cv2.LINE_AA)
        except:
            print("erreur")
    if mask is not None :
        cv2.imshow("mask",mask)
    cv2.imshow('image', frame)
    if cv2.waitKey(10)&0xFF==ord('q'):
        break
VideoCap.release()
cv2.destroyAllWindows()