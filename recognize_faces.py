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

    # get the coordinates of the faces from the image, then calculate the vector number for each face
    print("[info] recognizing faces...")
    img, faces, boxes = face_detection(image)
    print(data["names"])
    for face in faces:
        h, w = face.shape[:2]
        box = (0, w-1, h-1, 0)
        rgb_face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(rgb_face, [box])
        matches = face_recognition.compare_faces(data["encodings"], encoding[0], tolerance=0.5)
        print(matches)
        cv2.imshow('face', face)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        

    

img = cv2.imread('testimg/face_test1.jpg')
recognize(img)
