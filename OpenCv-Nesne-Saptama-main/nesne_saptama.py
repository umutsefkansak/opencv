import cv2
import numpy as np

cap = cv2.VideoCapture("hsv.mp4")


def nothing(x):
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",(512,512))
cv2.createTrackbar("Lower-H","Trackbars",0,180,nothing)
cv2.createTrackbar("Lower-S","Trackbars",0,255,nothing)
cv2.createTrackbar("Lower-V","Trackbars",0,255,nothing)


cv2.createTrackbar("Upper-H","Trackbars",0,180,nothing)
cv2.createTrackbar("Upper-S","Trackbars",0,255,nothing)
cv2.createTrackbar("Upper-V","Trackbars",0,255,nothing)

cv2.setTrackbarPos("Upper-H","Trackbars",180)
cv2.setTrackbarPos("Upper-S","Trackbars",255)
cv2.setTrackbarPos("Upper-V","Trackbars",255)


while True:
    ret,frame = cap.read()
    if ret == False:
        break
    frame = cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    lh = cv2.getTrackbarPos("Lower-H","Trackbars")
    ls = cv2.getTrackbarPos("Lower-S","Trackbars")
    lv = cv2.getTrackbarPos("Lower-V","Trackbars")

    uh = cv2.getTrackbarPos("Upper-H","Trackbars")
    us = cv2.getTrackbarPos("Upper-S","Trackbars")
    uv = cv2.getTrackbarPos("Upper-V","Trackbars")


    lower_color = np.array([lh,ls,lv])
    upper_color = np.array([uh,us,uv])

    mask = cv2.inRange(hsv,lower_color,upper_color)
    bit = cv2.bitwise_and(frame,frame,mask=mask)



    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("bit",bit)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()