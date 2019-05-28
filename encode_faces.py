import cv2
from imutils import paths
import face_recognition
import pickle
import os
from detect_faces import single_face_detection, face_detection
from time import time

def encode_faces():
    fnStart = time()
    dataset = 'sample_dataset'
    encodings_file = 'encodings.pickle'
    detection_method = 'cnn'

    # get the paths for the images in the dataset
    imgPaths = list(paths.list_images(dataset))

    # initializing a list of known encodings and names
    knownEncodings = []
    knownNames = []

    for (i, imgPath) in enumerate(imgPaths):
        start = time()
        # getting the name from the image path
        name = imgPath.split(os.path.sep)[-2]

        # reading the image and converting it into RGB (converting to rgb is useful for dlib, however opencv dnn is able to process both RGB and BGR so it does not really matter which one is used)
        img = cv2.imread(imgPath)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # boxes = face_recognition.face_locations(rgb, model=detection_method)
        a, b, boxes = face_detection(rgb)
        # (sX, eX, eY, sY) = boxes[0]

        # turning the bounding boxes from the faces and turning them into a 128 number vector
        encodings = face_recognition.face_encodings(rgb, boxes)

        # looping over the encodings
        for encoding in encodings:
            # appending the name and the encoding to the list of knownEncodings and knownNames
            knownEncodings.append(encoding)
            knownNames.append(name)
        
        print("[info] processed image {}/{} in {:.3f} seconds".format(i+1, len(imgPaths), time()-start))
    
    print('[info] serializing encodings...')
    data = {"encodings": knownEncodings, "names": knownNames}
    f = open(encodings_file, "wb")
    f.write(pickle.dumps(data))
    f.close()
        
    print("[info] encode faces done in {:.3f} seconds".format(time()-fnStart))

encode_faces()

# cv2.imshow(name, img[sY:eY, sX:eX])
# cv2.waitKey(0)
# cv2.destroyAllWindows()