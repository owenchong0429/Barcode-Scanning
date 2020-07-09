import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
rec = cv2.VideoWriter('output.mp4',fourcc ,20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret==True):
        rec.write(frame)
        cv2.imshow('output',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyALLWindows()