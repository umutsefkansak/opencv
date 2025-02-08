import cv2
import numpy as np



cap = cv2.VideoCapture("line.mp4")

while True:

    ret,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    copy = frame.copy()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([18,94,140],np.uint8) # Değerler için hsv range for renk_adi
    upper_yellow = np.array([48,255,255],np.uint8)

    mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
    #output = cv2.bitwise_and(frame,frame,mask=mask)
    edges = cv2.Canny(mask,75,250)

    lines = cv2.HoughLinesP(edges,1,np.pi/180,25,maxLineGap=50) # ro ve teta değerleri

    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5) #koordinatlar,renk,kalınlık


    #cv2.imshow("edges",edges)
    cv2.imshow("cap",frame)
    cv2.imshow("copy",copy)
    cv2.imshow("hsv",mask) # ekranda çıkan görüntüde de sarı olmasını istiyorsak output degiskenini gosteririz

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()