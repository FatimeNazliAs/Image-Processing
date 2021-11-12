import cv2

cap = cv2.VideoCapture("1.mp4")

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAYQ)

    if ret==False:
        break


    cv2.imshow("Video",frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
