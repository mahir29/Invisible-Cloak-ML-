import cv2

#This is my webCam
cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret,back=cap.read() #Here is simply reading
    if ret:
        #back is what camera reading
        cv2.imshow("image",back)
        if cv2.waitKey(100)==ord('q'):
            #save the image
            cv2.imwrite("image.jpg",back)
            break

cap.release()
cv2.destroyAllWindows()
