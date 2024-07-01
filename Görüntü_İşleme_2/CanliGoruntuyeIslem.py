from cv2 import*
from numpy import*

kamera=VideoCapture(0)

while True:
    ret,goruntu=kamera.read()

    rectangle(goruntu,(200,100),(462,450),(0,0,255),3)
    putText(goruntu, "TheDenizhan", (160,85), FONT_HERSHEY_SCRIPT_COMPLEX, 2, (25, 25, 255), 2)

    imshow("goruntu",goruntu)

    if waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
destroyAllWindows()