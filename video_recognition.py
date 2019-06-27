import cv2
from recognize_faces import recognize
from time import time

def recognize_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if (cap.isOpened()== False): 
        print("Error opening video stream or file\n")
        return 0
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_ct = 0
    iteration = 0
    attendance = []
    while True and frame_ct < length-1 and iteration <= 5:
        _, frame = cap.read()
        h, w = frame.shape[:2]
        if frame_ct % 24 == 0:
            iteration += 1
            frame, names = recognize(frame)
            # frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            attendance.extend(names)

            #showing the result
            cv2.putText(frame, "frame = " + str(frame_ct), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            # cv2.imwrite(str(time())+".jpg", frame)

            cv2.imshow('frame', frame)

            #exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        frame_ct += 1
    attendance = list(set(attendance))
    for (i, name) in enumerate(attendance):
        if 'unknown' in name:
            del attendance[i]
            print('There are undetected students')
            
    cap.release()
    cv2.destroyAllWindows()
    return attendance

# recognize_video('test_vid/classroom2.mp4')