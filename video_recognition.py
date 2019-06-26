import cv2
from recognize_faces import recognize

def recognize_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
        return []
    frame_ct = 0
    attendance = []
    while True and frame_ct <= 50:
        _, frame = cap.read()
        h, w = frame.shape[:2]
        frame_ct += 1
        if frame_ct % 10 == 0:
            frame, names = recognize(frame)
            frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            attendance.extend(names)

            #showing the result
            cv2.putText(frame, "frame = " + str(frame_ct), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)
            frame = cv2.resize(frame, (int(w/3),int(h/3)))

            cv2.imshow('frame', frame)

            #exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    attendance = list(set(attendance))
    for (i, name) in enumerate(attendance):
        if 'unknown' in name:
            del attendance[i]
            print('There are undetected students')
            
    cap.release()
    cv2.destroyAllWindows()
    return attendance
