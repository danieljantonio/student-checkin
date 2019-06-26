import cv2 
import recognize_faces
import numpy as np

def recog_vid(video):
    cap = cv2.VideoCapture(video)
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
        return []
    
    count = 0
    present_list = []
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True and count<10:
            count = count + 1
            if count%2 == 0:
                frame, names = recognize_faces.recognize(frame)
                present_list.extend(names)
            
        # Break the loop
        else: 
            break
       
           
    # When everything done, release the video capture object
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()

    present_list = list(set(present_list))
    return present_list

# print(recog_vid("test_vid/classroom1.avi"))