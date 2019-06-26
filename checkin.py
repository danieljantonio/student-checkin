# checkin system
# Dummy file for now
#  try standardizing image sizes
import csv
import cv2
import numpy as np 
import recognize_faces
def getNameList(filename):
    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    
    return (data[0])


# name , date and image needs to be user input
def checkIn(names, cName, date):
    print('checkin/'+cName+'.txt')
    nameList = getNameList('checkin/'+cName+'.txt')
    date = date.replace("/","_")
    check_list = cName + '_' + date + '.txt'
    # image = cv2.imread('testing_images/test1.jpg',1)
    
    # _, names = recognize_faces.recognize(image)
    # names = list(set(names))
    # print(names)
    for name in names:
        if name in nameList:
            print(nameList[nameList.index(name)])
            nameList[nameList.index(name)] = nameList[nameList.index(name)] + "  Present"
  
    # print(nameList)
    # print("checkin/"+check_list)
    f = open("checkin/"+check_list,"w+")

    for line in nameList:
        f.write(str(line + ',').rstrip('\n'))
    f.close()
    print("checkin/"+check_list+" file created")
