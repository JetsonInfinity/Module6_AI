#Module Easypip3
import cv2
import cvlib
import cvlib as cv #detects object
from cvlib.object_detection import draw_bbox #lib to highlight the objects
import xarm

#arm = xarm.Controller('USB')

labels = [] 
input_choice ='-'
while input_choice not in ['c','p']:
    input_choice= input("Welcome to the first AI Module!\n Please type in c to use you're live camera, or p to upload existing photo: ")


if input_choice == 'c':
    while True:
        image_path ="/Users/saadsalman/Documents/GitHub/Module6_AI/testpic.jpeg"
        image = cv2.imread(image_path)

        bbox, label, conf = cv.detect_common_objects(image)

        output_image = draw_bbox(image,bbox,label,conf) #draws box around detected object with label named 
        cv2.imshow("Object Detection", output_image)

        for item in label:
            labels.append(item)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if input_choice == 'p':
    video = cv2.VideoCapture(1) #sets video as an object
    
    while True:
        ret, frame=video.read() #captures single frame from video, where frame acts like image data array
        bbox, label, conf =cv.detect_common_objects(frame) #performs object detection on "frame" while returning box cor, labels & confident levels


        output_image = draw_bbox(frame,bbox,label,conf) #draws box around detected object with label named 
        cv2.imshow("Object Detection", output_image)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
        for item in label:
            if item in labels:
                pass
            else:
                labels.append(item)


print(labels)


#object_classes = cvlib.object_detection.classes
#print(object_classes)

#arm.setPosition([[1,240],[2, 515],[3,840],[4,280],[5,475],[6,650]])