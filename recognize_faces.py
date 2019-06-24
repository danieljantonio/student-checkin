import cv2
import numpy as np
import face_recognition
import pickle
from time import time
from detect_faces import face_detection

def recognize(image):
    # load known faces and encodings
    encoding_file = 'encodings.pickle'
    print("[info] loading encodings... ")
    data = pickle.loads(open(encoding_file, "rb").read())

    # convert image to rgb for dlib
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # get the coordinates of the faces from the image, then calculate the vector number for each face
    print("[info] recognizing faces...")
    img, faces, boxes = face_detection(rgb_image)
    encodings = face_recognition.face_encodings(rgb_image, boxes)
    print(boxes)

    names = []
    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding, tolerance=0.4)
        name = "unknown"
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            name = max(counts, key=counts.get)
        names.append(name)
    print(names)
    for ((sX, eX, eY, sY), name) in zip(boxes, names):
        cv2.rectangle(image, (sX, sY), (eX, eY), (0,255,0), 2)
        y = sX - 15 if sX - 15 > 15 else sX + 15
        cv2.putText(image, name, (sX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 2)
    
    cv2.imshow('', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    

img = cv2.imread('testimg/face_test1.jpg')
recognize(img)
