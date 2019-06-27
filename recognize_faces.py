import cv2
import numpy as np
import face_recognition
import pickle
from time import time
from detect_faces import face_detection

encoding_file = 'jyencodings.pickle'
print("[info] loading encodings... ")
data = pickle.loads(open(encoding_file, "rb").read())

def recognize(image):
    # load known faces and encodings

    # get the coordinates of the faces from the image, then calculate the vector number for each face
    print("[info] recognizing faces...")
    img, faces, boxes = face_detection(image)
    # cv2.imwrite(str(time())+".jpg", img)
    # print(data["names"])
    start = time()
    names = []
    for face in faces:
        h, w = face.shape[:2]
        box = (0, w-1, h-1, 0)
        rgb_face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(rgb_face, [box], num_jitters=2)
        matches = face_recognition.compare_faces(data["encodings"], encoding[0], tolerance=0.4)
        name = "unknown"
        # print(matches)
        if True in matches:
            matched = [i for (i, match) in enumerate(matches) if match]
            counts = {}

            for i in matched:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            name = max(counts, key=counts.get)
        names.append(name)
    for ((sX, eX, eY, sY), name) in zip(boxes, names):
        cv2.rectangle(image, (sX, sY), (eX, eY), (0,255,0), 2)
        y = sY - 15 if sY - 15 > 15 else sY + 15

        h, w = image.shape[:2]
        if h < 1000 or w < 1000:
            cv2.putText(image, name, (sX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 2)
        else:
            cv2.putText(image, name, (sX, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)
    
    # cv2.imwrite(str(time())+".jpg", image)
    h, w = image.shape[:2]
    # cv2.imshow('face', cv2.resize(image,(int(w/3), int(h/3))))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print("[info] face recognition took {:.3f} seconds".format(time()-start))
    return image, list(set(names))
    

    

# img = cv2.imread('testimg/face_test2.jpg')
# recognize(img)
