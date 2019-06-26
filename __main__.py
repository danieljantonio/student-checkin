
# import the functions
# import detect_faces
import encode_faces
import recognize_faces
import cv2
import checkin
import recognize_videos
import video_recognition

if __name__ == '__main__':
    print('main')

    # action options
    # 1. add image to encoding (run encode()) //the user is assumed to add the file to the dataset folder
    # 2. run recognition on image
    # 3. run recognition on video

    while True:
        print("\n")
        print("Choose Option\n1. Add image to encoding\n2. run recognition on image\n3. run recognition on video\n4. Run CheckIn on image\n\n0.Exit\nChoice: ")
        choice = input()
        print("\n")
        if choice == "1":
            # 1. add image to encoding (run encode()) //the user is assumed to add the file to the dataset folder
            print("Please ensure that you have added the images to the dataset folder.\nFor more information please refer to the Read Me\nEnter any key to Continue")  
            input()
            encode_faces.encode()
        
        elif choice == "2":
            # Run facial recognition on specified image
            print("Please input image path")
            img = cv2.imread(input())
            if img is not None:
                recognize_faces.recognize(img)
            else:
                print("Invalid Image path\nRedirected to menu")
        
        elif choice == "3":
            print("# 4. Input video path")
            vidPath = input()
            names = video_recognition.recognize_video(vidPath)
            print("Detected Students: ")
            print(names)
        
        elif choice == "4":
            print("Please input image path")
            img = cv2.imread(input(),1)
            if img is None:
                print("Invalid Image path\nRedirected to menu")
                continue

            print("Class name(currently available: CSC3201, CSC3202)")
            cName = input()
            
            print("Date ")
            date = input()

            _, names = recognize_faces.recognize(img)
            # remove redundant elements
            names = list(set(names))
            checkin.checkIn(names, cName, date)
            
        elif choice == "0":
            print("exit")
            break
        else:
            print("Pick valid choices")