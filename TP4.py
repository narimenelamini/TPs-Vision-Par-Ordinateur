import cv2
import numpy as np

cap = cv2.VideoCapture("output.avi")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))


fourcc = cv2.VideoWriter_fourcc('M','j','P','G')
out = cv2.VideoWriter('outputGRAY.avi', fourcc,20,(frame_width,frame_height))


while cap.isOpened :
    ret,frame = cap.read()
    if not ret:
        print("Erreur Read")
        break
    #img_hsv = cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    out.write(frame)
    cv2.imshow("image", frame)
    if cv2.waitKey(20)  & 0xFF == ord('a'): #temps d'echantiollnage
        break

out.release()
cap.release()
cv2.destroyAllWindows()
