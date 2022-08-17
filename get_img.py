import cv2

cap = cv2.VideoCapture(0)
cap.set(3,416)  #width
cap.set(4,416)  #height

cnt = 0
t_gap = 50

while(1):
    ret, frame = cap.read()
    if (cnt % t_gap == 0):
        cv2.imwrite('img.jpg', frame)
    cnt += 1
    cv2.waitKey(1)

    k = cv2.waitKey(1) & 0xff
    if k == 27:    #'ESC'
        break

    
cap.release()
