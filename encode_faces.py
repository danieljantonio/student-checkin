import cv2
from imutils import paths
import face_recognition
import pickle
import os
from detect_faces import single_face_detection

def encode_faces():
    dataset = 'sample_dataset'
    encodings = 'encodings.pickle'
    detection_method = 'cnn'

    # get the paths for the images in the dataset
    imgPaths = list(paths.list_images(dataset))

    # initializing a list of known encodings and names
    knownEncodings = []
    knownNames = []

    for (i, imgPath) in enumerate(imgPaths):
        print("[info] processing image {}/{}".format(i+1, len(imgPaths)))
        # getting the name from the image path
        name = imgPath.split(os.path.sep)[-2]
        print(imgPath)

        # reading the image and converting it into RGB
        img = cv2.imread(imgPath)
        # rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # boxes = face_recognition.face_locations(rgb, model=detection_method)
        a, b, boxes = single_face_detection(img)
        (sX, eX, eY, sY) = boxes
        # cv2.imshow(name, img[sY:eY, sX:eX])
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        

encode_faces()