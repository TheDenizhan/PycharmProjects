from cv2 import*
from numpy import*

image=imread("Morfolojjik.png")

kernel=ones((3,3),uint8)                            #kernel...

dilation=dilate(image,kernel,iterations=1)          #resimdeki beyazları genişletme
erosion=erode(image,kernel,iterations=1)            #resimdeki beyazları daraltma
dilation2=dilate(erosion,kernel,iterations=1)       #resimdeki beyazları ilk önce daraltıp daha sonra genişletme
opening=morphologyEx(image,MORPH_OPEN,kernel)       #resimdeki beyazları ilk önce daraltıp daha sonra genişletme
closing=morphologyEx(image,MORPH_CLOSE,kernel)      #resimdeki beyazları ilk önce genişletip daha sonra daraltma
gradyan=morphologyEx(image,MORPH_GRADIENT,kernel)   #genişlettiğimiz resimden daraltığımız resmi çıkartma
tophat=morphologyEx(image,MORPH_TOPHAT,kernel)      #orjinal resimden openning işlemini çıkartma
blackhat=morphologyEx(image,MORPH_BLACKHAT,kernel)  #orjinal işlemden closing işlemini çıkartma
imshow("orji",image)
imshow("dilations",dilation)
imshow("erossion",erosion)
imshow("dilations2",dilation2)
imshow("openning",opening)
imshow("closing",closing)
imshow("gradyan",gradyan)
imshow("tophat",tophat)
imshow("blackhat",blackhat)


waitKey(0)
destroyAllWindows()