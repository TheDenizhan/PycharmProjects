from cv2 import*
from numpy import *

recognizer =cv2.face.LBPHFaceRecognizer_create()

recognizer.read('code/code.yml')
cascadePath="haarcascade_frontalface_default.xml"
faceCascade=CascadeClassifier(cascadePath);
font=FONT_HERSHEY_SIMPLEX
cam2=VideoCapture(0)



while(True):
    ret,img2=cam2.read()
    gray =cvtColor(img2,COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE)

    for(x,y,w,h) in faces:
        rectangle(img2,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        Id,confidence= recognizer.predict(gray[y:y+h,x:x+w])

        if(Id==1):
            Id = "Hasan"
            print(Id)

        else:
            Id = "  ?"
            print(Id)

        rectangle(img2, (x - 22, y - 90), (x + w + 22, y - 22), (255,0, 0), -1)
        putText(img2, str(Id), (x, y - 40), font, 2, (255, 255, 255), 3)

    imshow('Yuz Tanima', img2)

    if waitKey(10)& 0xFF == ord('q'):
            break

cam2.release()
destroyAllWindows()