import numpy as np
import cv2

imgpath = r"C:/Users\SAL\Desktop/haarcascade_eye.xml"
img_pathh=r"C:Users\SAL\Documents/GitHub/Module6_AI/testqw.jpg"

new_case = cv2.CascadeClassifier(imgpath)

img_new =cv2.imread(img_pathh)

gray=cv2.cvtColor(img_new, cv2.COLOR_BGR2GRAY)

faces = new_case.detectMultiScale(gray,1.01,7)
for (x,y,w,h) in faces:
    img_new = cv2.rectangle(img_new,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img_new',img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()