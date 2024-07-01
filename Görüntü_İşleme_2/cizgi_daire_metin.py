from cv2 import*
from numpy import*

image1=zeros((300,300,3),"uint8")

line(image1,(0,0),(100,100),(25,25,255),4)      #çizgi yazma
line(image1,(300,0),(200,200),(25,25,255),4)
line(image1,(0,300),(100,100),(25,25,255),4)
line(image1,(300,300),(200,200),(25,25,255),4)
circle(image1,(150,150),50,(25,25,255),4)       #daire
putText(image1,"TheDenizhan",(50,35),FONT_HERSHEY_COMPLEX,1,(25,25,255),1)  #metin yazma
#putText(değişken,"yazılacak yazı",(x,y)koordinatları,yazı şekli,yazı boyutu,renk,kalınlık
imshow("image",image1)

waitKey(0)
destroyAllWindows()