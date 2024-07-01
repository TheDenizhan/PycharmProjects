from cv2 import*
from os import*
from numpy import*
from face_recognition import*
from PIL import Image

recognizer = cv2.face.EigenFaceRecognizer_create()
detector = CascadeClassifier("haarcascade_frontalface_default.xml");

def getImagesAndLaabels(path):

    imagePath=[os.path.join(path,f) for f in listdir(path)]

    faceSamples =[]

    ids =[]

    for imagePath in imagePath:

        PIL_img = Image.open(imagePath).convert('L')

        img_numpy=array(PIL_img,'uint8')

        id =int(os.path.split(imagePath)[-1].split("_")[1])
        print(id)

        faces =detector.detectMultiScale(img_numpy,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE)

        for (x,y,w,h) in faces:

            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids


faces,ids=getImagesAndLaabels('pic')
recognizer.train(faces,array(ids))
recognizer.load('code/code.yml')