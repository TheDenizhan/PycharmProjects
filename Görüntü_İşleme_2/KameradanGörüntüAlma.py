from cv2 import *
from numpy import *

#Kameradan alınan canlı görüntünün kayıt edilmesi
camera=VideoCapture(0)
width = int(camera.get(CAP_PROP_FRAME_WIDTH))
height = int(camera.get(CAP_PROP_FRAME_HEIGHT))
print(width,height)
fourcc=VideoWriter_fourcc(*'MP4V')      #Kameradan alınacak görüntünün hangi türde kayıt edileceğini belirler
writer=VideoWriter("kayit.mp4",fourcc,20,(width,height))
#sayı küçüldükçe video hızı azalır,sayı büyükçe video hızı artar
while True:
    ret,frame=camera.read()
    writer.write(frame)
    imshow("Kamera",frame)

    if  waitKey(10)  & 0xFF == ord('q'):
        break

camera.release()
writer.release()
destroyAllWindows()
