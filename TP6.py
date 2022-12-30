import cv2
import numpy as np

lo = np.array([95,100,50])
hi = np.array([115,255,255])

def detect_inrange(image, surface):
    points =[]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image = cv2.blur(image, (5,5))
    mask = cv2.inRange(image, lo,hi) #récupère une image binaire
    mask = cv2.erode(mask, None , iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    elements = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    elements = sorted(elements, key = lambda x:cv2.contourArea(x), reverse = True)
    for element in elements:
        if cv2.contourArea(element) > surface:
            ((x,y), rayon) = cv2.minEnclosingCircle(element)
            points.append(np.array([int(x), int(y), int(rayon), int(cv2.contourArea(element))]))
        else:
            break

    return image, mask , points


videoCap = cv2.VideoCapture(0)
while(True):
    ret,frame = videoCap.read()
    cv2.flip(frame, 1, frame) #inverser les axes x et y : -1 : inverser y , 1 : iverser x, 0 : les 2
    image, mask, points  = detect_inrange(frame, 1000)
    cv2.circle(image, (100,100), 20, (0,255,0),5)
    print(image[100,100])
    if(len(points)>0):
        cv2.circle(frame, points[0][0], points[0][1], points[0][2],(0,0,255), 2)
        cv2.putText(frame, str(points[0][3]), (points[0][0], points[0][1]), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)

    if mask is not None:
        cv2.imshow("mask", mask)
    cv2.imshow('image', image)
    if cv2.waitKey(20)  & 0xFF == ord('a'): #temps d'echantiollnage
        break

videoCap.release()
cv2.destroyAllWindows()