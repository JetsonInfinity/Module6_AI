import cv2
import numpy as np
import matplotlib.pyplot as plt

# Define the path to the arm cascade XML file
arm_cascade_path = r"C:\Users\SAL\Desktop\New-Mod\classifier\cascade-arm.xml"

# Load the arm cascade classifier
arm_cascade = cv2.CascadeClassifier(arm_cascade_path)

# Read the image
img_path = r"C:\Users\SAL\Documents\GitHub\Module6_AI\testqw.jpg"
img = cv2.imread(img_path)

# Function to detect arm
def detect_arm(img):
    arm_img = img.copy()
    arm_rect = arm_cascade.detectMultiScale(arm_img,
                                            scaleFactor=1.2,
                                            minNeighbors=5)

    for (x, y, w, h) in arm_rect:
        cv2.rectangle(arm_img, (x, y),
                      (x + w, y + h), (255, 255, 255), 10)
    return arm_img

# Detecting the arm
arm_detected = detect_arm(img)

# Displaying and saving the image
plt.imshow(arm_detected)
plt.show()
cv2.imwrite('arm_detected.jpg', arm_detected)