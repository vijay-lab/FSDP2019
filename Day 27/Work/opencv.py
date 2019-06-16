# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 19:37:27 2019

@author: TAPAN

Q2. Facial Recognition + OpenCV Python

Facial recognition is a biometric software application capable of uniquely identifying or verifying a person by comparing and analyzing.

Things that you need in this project: OpenCV and face_recognition

The project is mainly a method for detecting faces in a given image by using OpenCV-Python and 
face_recognition module. The first phase uses camera to capture the picture of our faces which 
generates a feature set in a location of your PC.

• The face_recognition command lets you recognize faces in a photograph or folder full for photographs.

It has two simple commands

Face_ recognition- Recognise faces in a photograph or folder full for photographs.
face_detection - Find faces in a photograph or folder full for photographs.
For face recognition, first generate a feature set by taking few image of your face and create a directory 
with the name of person and save their face image.


Then train the data by using the Face_ recognition module.By Face_ recognition module the trained data is 
stored as pickle file (.pickle).

By using the trained pickle data, we can recognize face.

The main flow of face recognition is first to locate the face in the picture and the compare the picture 
with the trained data set.If the there is a match, it gives the recognized label.
(Ref: https://github.com/sriram251/-face_recognition)
"""

import numpy as np
import os
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
path = "D:\\dataset\\"# path were u want store the data set
id = input('enter user name')

try:
    # Create target Directory
    os.mkdir(path+str(id))
    print("Directory " , path+str(id),  " Created ") 
except FileExistsError:
    print("Directory " , path+str(id) ,  " already exists")
sampleN=0;

while 1:

    ret, img = cap.read()
    frame = img.copy()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        sampleN=sampleN+1;

        cv2.imwrite(path+str(id)+ "\\" +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.waitKey(100)

    cv2.imshow('img',img)

    cv2.waitKey(1)

    if sampleN > 40:

        break

cap.release()

cv2.destroyAllWindows()

# training the model
import cv2
import imutils.paths as paths

import face_recognition
import pickle
import os
dataset = "D:\\dataset\\"# path of the data set 
module = "D:\\encodings\\encoding1.pickle" # were u want to store the pickle file 

imagepaths = list(paths.list_images(dataset))
knownEncodings = []
knownNames = []
for (i, imagePath) in enumerate(imagepaths):
    print("[INFO] processing image {}/{}".format(i + 1,len(imagepaths)))
    name = imagePath.split(os.path.sep)[-2]
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)	
    boxes = face_recognition.face_locations(rgb, model= "hog")
    encodings = face_recognition.face_encodings(rgb, boxes)
    for encoding in encodings:
       knownEncodings.append(encoding)
       knownNames.append(name)
       print("[INFO] serializing encodings...")
data = {"encodings": knownEncodings, "names": knownNames}
output = open(module, "wb") 
pickle.dump(data, output)
output.close()


import imutils
import numpy as np
import pickle
import cv2
import face_recognition


def main(): 
    encoding = "D:\\encodings\\encoding1.pickle"
    data = pickle.loads(open(encoding, "rb").read())
    print(data)
    cap = cv2.VideoCapture(0)
  
    if cap.isOpened :
        ret, frame = cap.read()
    else:
         ret = False
    while(ret):
      ret, frame = cap.read()
      rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      rgb = imutils.resize(frame, width=400)
      r = frame.shape[1] / float(rgb.shape[1])

      boxes = face_recognition.face_locations(rgb, model= "hog")
      encodings = face_recognition.face_encodings(rgb, boxes)
      names = []
   
      for encoding in encodings:
                matches = face_recognition.compare_faces(np.array(encoding),np.array(data["encodings"]))
                name = "Unknown"
               
                if True in matches:
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}
                   
                    
                    for i in matchedIdxs:
                                  name = data["names"][i]
                                  counts[name] = counts.get(name, 0) + 1
                                  name = max(counts, key=counts.get)
                names.append(name)
                
      for ((top, right, bottom, left), name) in zip(boxes, names):
          top = int(top * r)
          right = int(right * r)
          bottom = int(bottom * r) 
          left = int(left * r)
          cv2.rectangle(frame, (left, top), (right, bottom),(0, 255, 0), 2)
          y = top - 15 if top - 15 > 15 else top + 15
          cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
      cv2.imshow("Frame", frame)
      if cv2.waitKey(1) == 27:
          break                                                

    cv2.destroyAllWindows()

    cap.release()
    
if __name__ == "__main__":
    main()