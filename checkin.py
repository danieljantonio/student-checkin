# checkin system
# Dummy file for now
#  try standardizing image sizes
import csv
import cv2
import numpy as np 
import recognize_faces
import datetime
def getNameList(filename):
    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    
    return (data[0])


# name , date and image needs to be user input
def checkIn(names, cName):
    # print('checkin/'+cName+'.txt')
    nameList = getNameList('checkin/'+cName+'.txt')
    # date = date.replace("/","_")
    date = str(datetime.date.today())
    check_list = cName + '_' + date + '.txt'
    # image = cv2.imread('testing_images/test1.jpg',1)
    
    # _, names = recognize_faces.recognize(image)
    # names = list(set(names))
    # print(names)
    present = []
    absent = []

    for name in nameList:
        if name in names:
            present.append(name)
        else:
            absent.append(name)

    # for name in names:
    #     if name in nameList:
    #         print(nameList[nameList.index(name)])
    #         nameList[nameList.index(name)] = nameList[nameList.index(name)] + "Present"
  
    # print(nameList)
    # print("checkin/"+check_list)
    f = open("checkin/"+check_list,"w+")

    # for line in nameList:
    #     f.write(str(line + ',').rstrip('\n'))

    f.write("Students present on " + date + " for class " + cName + " ({}/{})".format(len(present), len(nameList)) + "\n")
    for name in present:
        f.write(str(name) + '\n')
    f.write("\n\nStudents absent on " + date + " for class " + cName + " ({}/{})".format(len(absent), len(nameList)) + "\n")
    for name in absent:
        f.write(str(name) + '\n')
        
    f.close()
    print("checkin/"+check_list+" file created")
