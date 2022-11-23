import cv2
import numpy as np


lower_blue = np.array([100,75,25])
upper_blue = np.array([130,255,255])

lower_red = np.array([0,170,50])
upper_red = np.array([5,255,255])

lower_red2 = np.array([170,160,50])
upper_red2 = np.array([180,255,255])


cap = cv2.VideoCapture('film.mp4')
w = int(cap.get(3))
h = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('kolory.mp4', fourcc, 50.0, (w, h), True)


while(cap.isOpened()):

    ret, frame = cap.read()

    if not ret:
        print("Koniec")
        break
        
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask_blue + mask_red + mask_red2
    
    res = cv2.bitwise_and(frame,frame, mask= mask)
    out.write(res)
    cv2.imshow('film',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows() 