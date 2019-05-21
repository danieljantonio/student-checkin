import cv2
import numpy as np

def face_detection(img, padding=0.05):
    faces = []

    # defining models
    prototxt_path = './model/deploy.prototxt'
    caffemodel_path = './model/res10_300x300_ssd_iter_140000.caffemodel'

    # reading the models
    model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

    # detect faces
    (h, w) = img.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    model.setInput(blob)
    detections = model.forward()
    print(detections.shape)

    # loop through all possible 
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # check if confidence > 0.5
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (sX, sY, eX, eY) = box.astype('int')
            dX = int((eX - sX) * padding)
            dY = int((eY - sY) * padding)

            sX = max(0, sX - dX)
            sY = max(0, sY - dY)
            eX = min(w, eX + dX)
            eY = min(h, eY + dY)

            faces.append(img[sY:eY, sX:eX])
            cv2.rectangle(img, (sX, sY), (eX, eY), (0, 255, 0), 2)

    return img, faces

img = cv2.imread('src/face_test1.jpg')
faces_img, faces = face_detection(img, 0.1)
cv2.imshow('faces', faces_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

for face in faces:
    cv2.imshow('face', face)
    cv2.waitKey(0)
    cv2.destroyAllWindows()