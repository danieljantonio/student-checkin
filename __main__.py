
# import the functions
# import detect_faces
import encode_faces
import recognize_faces
import cv2
import checkin
import recognize_videos
import video_recognition
from time import sleep

if __name__ == '__main__':

    # action options
    # 1. add image to encoding (run encode()) //the user is assumed to add the file to the dataset folder
    # 2. run recognition on image
    # 3. run recognition on video

    while True:
        print("\n")
        print("Choose Option\n1. Add image to encoding\n2. Run recognition on image\n3. Run recognition on video\n4. Run CheckIn on image\n5. Run CheckIn on video\n\n0.Exit\nChoice: ")
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
                sleep(1)
                continue
        
        elif choice == "3":
            print("Input video path")
            vidPath = input()
            names = video_recognition.recognize_video(vidPath)
            if names == 0:
                print("Invalid Image path\nRedirected to menu")
                sleep(1)
                continue
            print("Detected Students: ")
            print(names)
        
        elif choice == "4":
            print("Please input image path")
            img = cv2.imread(input(),1)
            if img is None:
                print("Invalid Image path\nRedirected to menu")
                sleep(1)
                continue

            print("Class name(currently available: CSC3201, CSC3202)")
            cName = input()

            _, names = recognize_faces.recognize(img)
            checkin.checkIn(names, cName)
            
        elif choice == "5":
            print("Please input video path")
            vidPath = input()
            names = video_recognition.recognize_video(vidPath)
            if names == 0:
                print("Invalid Image path\nRedirected to menu")
                sleep(1)
                continue
            print("Class name(currently available: CSC3201, CSC3202)")
            cName = input()
            
            checkin.checkIn(names, cName)

        elif choice == "0":
            print("exit")
            break
        else:
            print("Pick valid choices")