# facerec.py
import cv2, sys, numpy, os
import json
size = 3
fn_dir2 = 'unknown'
fn_haar = 'haarcascade_frontalface_default.xml'
fn_dir = 'att_faces'
path2='/home/irum/Desktop/Face-Recognition/thakarrecog/unknown/UNKNOWNS'
path='/home/irum/Desktop/Face-Recognition/thakarrecog/att_faces'
# Part 1: Create fisherRecognizer
print('Training...')

# Create a list of images and a list of corresponding names
(images, lables, names, id) = ([], [], {}, 0)


for (subdirs, dirs, files) in os.walk(fn_dir):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(fn_dir, subdir)
        for filename in os.listdir(subjectpath):

            path = subjectpath + '/' + filename
            lable = id
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1



(im_width, im_height) = (112, 92)

# Create a Numpy array from the two lists above
(images, lables) = [numpy.array(lis) for lis in [images, lables]]

# OpenCV trains a model from the images

model = cv2.face.FisherFaceRecognizer_create()
model.train(images, lables)

# Part 2: Use fisherRecognizer on camera stream
haar_cascade = cv2.CascadeClassifier(fn_haar)
# Capturing camera feed
webcam = cv2.VideoCapture(0)
webcam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1920)
webcam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    # Reading Frames from live stream
    (rval, frame) = webcam.read()
    frame=cv2.flip(frame,1,0)
    #Convert frame into gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.GaussianBlur(gray, (21, 21), 0)
    # Resize the gary
    mini = cv2.resize(gray, (gray.shape[1] / size, gray.shape[0] / size))
    # Detecting the face
    faces = haar_cascade.detectMultiScale(mini,1.1, 5)
    for i in range(len(faces)):
        face_i = faces[i]
        (x, y, w, h) = [v * size for v in face_i]
        # Croping face
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))
        # Eualize Histogram
        eq = cv2.equalizeHist(face_resize)

        # Try to recognize the face

        prediction  = model.predict(eq)
        print ("Recognition Prediction" ,prediction)
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # Write the name of recognized face

        result = {
                'face': {

                 'distance': prediction,
                 'coords': {
                   'x': str(faces[0][0]),
                   'y': str(faces[0][1]),
                   'width': str(faces[0][2]),
                   'height': str(faces[0][3])
                    }
                }
              }
        print("1 Result of Over all Prediction" ,result)


        if prediction[0]>0 and prediction[0]<4 and prediction[1]<=500:

         result = {
            'face': {

             'distance': prediction[1],
             'coords': {
               'x': str(faces[0][0]),
               'y': str(faces[0][1]),
               'width': str(faces[0][2]),
               'height': str(faces[0][3])
                }
            }
          }

         dist = result['face']['distance']
         print("Known Face DISTANCE" , dist)

         cv2.putText(frame,
                 '%s - %.0f' % (names[prediction[0]],prediction[1]),
                 (x-10, y-10), cv2.FONT_HERSHEY_DUPLEX,1,(255, 255, 0))
         break

        else:
        #if prediction[0]<=0 and prediction[0]>=4 and prediction[1]>600:
         print("for prediction more than 600")
         print ("prediction", prediction )
         result = {
            'face': {

             'distance': prediction[1],
             'coords': {
               'x': str(faces[0][0]),
               'y': str(faces[0][1]),
               'width': str(faces[0][2]),
               'height': str(faces[0][3])
                }
            }
          }
         dist = result['face']['distance']
         print("UNKNOWN FACE" , dist)
         cv2.putText(frame,
              'Unknown',
              (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(255, 255, 0))
         pin=sorted([int(n[:n.find('.')]) for n in os.listdir(path2)
                if n[0]!='.' ]+[0])[-1] + 1
         cv2.imwrite('%s/%s.png' % (path2, pin), eq)

    cv2.imshow('OpenCV', frame)
    key = cv2.waitKey(10)
    if key == 27:
        break