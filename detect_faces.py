import cv2
import numpy as np
from time import time

def face_detection(img, padding=0.05):
    print(img.shape)
    start = time()
    faces = []
    img_original = img.copy()

    # defining models
    prototxt_path = './face_detection_model/deploy.prototxt'
    caffemodel_path = './face_detection_model/res10_300x300_ssd_iter_140000.caffemodel'

    # reading the models
    model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

    # detect faces
    (h, w) = img.shape[:2]
    if h < 1200 or w < 1200:
        print(300)
        blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    else:
        print(str(1200/900))
        # blob = cv2.dnn.blobFromImage(cv2.resize(img, (1200, 1200)), 1.0, (900, 900), (104.0, 177.0, 123.0))
        blob = cv2.dnn.blobFromImage(cv2.resize(img, (1200, 1200)), 1.0, (1200, 1200), (104.0, 177.0, 123.0))
    model.setInput(blob)
    detections = model.forward()
    # print(detections.shape)
    dlib_boxes = []

    # loop through all possible
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # check if confidence > 0.5
        if confidence > 0.6:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (sX, sY, eX, eY) = box.astype('int')
            dX = int((eX - sX) * padding)
            dY = int((eY - sY) * padding)

            sX = max(0, sX - dX)
            sY = max(0, sY - dY)
            eX = min(w, eX + dX)
            eY = min(h, eY + dY)

            faces.append(img_original[sY:eY, sX:eX])
            # cv2.imshow('faces', img_original[sY:eY, sX:eX])
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            dlib_boxes.append((sX, eX, eY, sY))
            cv2.rectangle(img, (sX, sY), (eX, eY), (0, 255, 0), 2)
    end = time()
    print("time taken {:.3f}".format(end-start))


    return img, faces, dlib_boxes

# get a single face from the image that has the biggest confidence, this will be used for the dataset as to ignore any possible false positives
def single_face_detection(img, padding=0.05):
    start = time()
    faces = []
    img_original = img.copy()

    # defining models
    prototxt_path = './face_detection_model/deploy.prototxt'
    caffemodel_path = './face_detection_model/res10_300x300_ssd_iter_140000.caffemodel'

    # reading the models
    model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

    # detect faces
    (h, w) = img.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    model.setInput(blob)
    detections = model.forward()

    max_conf = 0
    max_conf_index = 0
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        # check if confidence > 0.5
        if confidence > 0.5:
            if confidence > max_conf:
                max_conf = confidence
                max_conf_index = i
    
    box = detections[0, 0, max_conf_index, 3:7] * np.array([w, h, w, h])
    (sX, sY, eX, eY) = box.astype('int')
    dX = int((eX - sX) * padding)
    dY = int((eY - sY) * padding)

    sX = max(0, sX - dX)
    sY = max(0, sY - dY)
    eX = min(w, eX + dX)
    eY = min(h, eY + dY)

    faces.append(img_original[sY:eY, sX:eX])
    cv2.rectangle(img, (sX, sY), (eX, eY), (0, 255, 0), 2)

    end = time()
    # print(end-start)

    dlib_boxes = [(sX, eX, eY, sY)]

    return img, faces, dlib_boxes

# img = cv2.imread('testimg/face_test2.jpg')
# # img2 = cv2.imread('dataset/jy/jy1.jpg')
# # img3 = cv2.imread('dataset//jy/jy2.jpg')
# # img4 = cv2.imread('dataset/lishan/lish1.jpg')
# # img_arr = [img, img2, img3, img4]
# img_arr = [img]
# for img in img_arr:
#     facesimg, _, _ = face_detection(img)
#     cv2.imshow('faces', facesimg)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# faces_img, faces = single_face_detection(img, 0.1)
# print(faces[0].shape)

# count = 0
# for face in faces:
    # count += 1
    # cv2.imwrite(str(count) + ".png", face)
    # cv2.imshow('face', face)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# (sX, sY, eX, eY) = mine
# (sX, eX, eY, sY) = face_detection dlib


# img = cv2.imread('test_imgs/classroom1.jpg')
# facesimg, faces, _ = face_detection(img)
# cv2.imshow('faces', facesimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# for face in faces:
#     cv2.imshow('faces', face)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()