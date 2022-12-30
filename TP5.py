import cv2
import numpy as np

CHECKBOARD = (6,9)
creteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER , 30, 0.001)
objpoints = []
imgpoints = []
objp = np.zeros((1, CHECKBOARD[0] * CHECKBOARD[1], 3), np.float32)
objp[0,:,:2] = np.mgrid[0:CHECKBOARD[0], 0:CHECKBOARD[1]].T.reshape(-1,2)
prev_img_shape = None

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #determiner si il ya checkboard
    ret , corners = cv2.findChessboardCorners(gray, CHECKBOARD,
    cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK+ cv2.CALIB_CB_NORMALIZE_IMAGE)
    if ret == True :
        #determiner les points exaxts sur le checkboard
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners , (11,11), (-1,-1), creteria)
        imgpoints.append(corners2)
        img = cv2.drawChessboardCorners(img, CHECKBOARD, corners2, ret )


    cv2.imshow("image", img)
    if cv2.waitKey(100) &  0xFF == ord('0') :
        break

cv2.destroyAllWindows()
ret , mtx , dist , rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print("Camera matrix : \n")
print(mtx)
print("Distortion coeffiient : \n")
print(dist)
print("Rotation vectors : \n")
print(rvecs)
print("Translation Vectors: \n")
print(tvecs)

axis = np.float32([[3,0,0] , [0,0,-3]]).reshape(-1,3)
def draw(img , corners, imgpts):
    corner = tuple(np.unit16(corners[0]).ravel())
    img = cv2.line(img, corner, tuple(np.unit16(imgpts[0]).ravel()), (255,0,0), 5)
    img = cv2.line(img, corner, tuple(np.unit16(imgpts[0]).ravel()), (0,255,0), 5)
    img = cv2.line(img, corner, tuple(np.unit16(imgpts[0]).ravel()), (0,0,255), 5)
    return img

while True:
    ret, img  =  ret,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret , corners = cv2.findChessboardCorners(gray, CHECKBOARD,
    cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK+ cv2.CALIB_CB_NORMALIZE_IMAGE)
    if ret == True :
        corners1 = cv2.cornerSubPix(gray, corners , (11,11), (-1,-1), creteria)
        ret, rvecs, tvecs = cv2.solvePnP(objp, corners2, mtx,dist)
        imgpts = jac = cv2.projectPoints(axis,rvecs, mtx, dist)
        img = draw(img, corners2)
        img = cv2.drawChessboardCorners(img, CHECKBOARD, corners1, ret)
    cv2.imshow("img", img)
    if cv2.waitKey(100) &  0xFF == ord('0') :
        break

cv2.destroyAllWindows()
cap.release()