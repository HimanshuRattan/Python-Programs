#import numpy as np
import cv2
cap = cv2.VideoCapture(0)
#cap1=cv2.VideoCapture(1)
#cap2=cv2.VideoCapture(2)
while(True):
    ret, frame = cap.read()
    #ret, frame1 = cap1.read()+
    #ret, frame2 = cap2.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('frame',frame)
    #cv2.imshow('frame1',frame1)
    #cv2.imshow('frame2',frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()