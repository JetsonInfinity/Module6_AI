import cv2
import os
import time
import numpy as np

"""picture_path ="/Users/saadsalman/Documents/GitHub/Module6_AI"
#picture_path = r"C:\Users\SAL\Documents\GitHub\Module6_AI\stestpic.jpeg"
camera_num = 1
camera_brightness=190
course_of_pic=10
blury=500
grayImage = False
saveData= True
show_image = True
width=180
height=120

global countFolder
cap=cv2.VideoCapture(camera_num)
cap.set(3,640)
cap.set(4,480)
cap.set(10, camera_brightness)

count =0
countsave=0

def save_img_Data():
    global countFolder
    countFolder =0
    while os.path.exists(picture_path+ str(countFolder)):
        countFolder = countFolder + 1
    os.makedirs(picture_path+str(countFolder))

if saveData:save_img_Data()

while True:

    success, img =cap.read()
    img = cv2.resize(img,(width,height))
    if grayImage:img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    

    if saveData:
        blur = cv2.Laplacian(img,cv2.CV_64F).var()
        if count % course_of_pic==0 and blur >blury:
            nowTime = time.time()
            cv2.imwrite(picture_path+str(countFolder)+'/' + str(countsave)+"_"+str(int(blur))+"_"+str(nowTime)+".png", img)
            countsave+=1
        count+=1

    if show_image:
        cv2.imshow("Image",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
destroyAllWindows()"""