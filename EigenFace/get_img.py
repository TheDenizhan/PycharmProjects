from cv2 import*
vid_cam = VideoCapture(0)
face_detector =CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = 1
count =0
while(True):
    _,img_frame=vid_cam.read()
    gray=cvtColor(img_frame,COLOR_BGR2GRAY)

    faces=face_detector.detectMultiScale(gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE)

    for(x,y,w,h) in faces:
        rectangle(img_frame,(x,y),(x+w,y+h),(0,0,255),2)

        count+=1

        imwrite("pic/veri_"+str(face_id)+'_'+str(count)+".jpg",gray[y:y+h,x:x+w])
        imshow("frame",img_frame)

    if waitKey(1)& 0xFF == ord('q'):
        break

    elif count>50:
        break


vid_cam.release()
destroyAllWindows()