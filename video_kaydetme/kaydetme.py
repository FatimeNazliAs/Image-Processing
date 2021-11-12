import cv2

cap = cv2.VideoCapture(0)



filename ="C:\betul-pc\PycharmProjects\Goruntu_Isleme\webcam.avi"
codec = cv2.VideoWriter_fourcc('W','M','V','2')
frameRate=20
resolution=(640,480)#video kaydedici boyutu
videoOutput = cv2.VideoWriter(filename, codec,frameRate, resolution)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    videoOutput.write(frame)     

    cv2.imshow("Webcam Live",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
