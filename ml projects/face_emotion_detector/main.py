from fer import FER
import cv2

img=cv2.imread('happy.jpg')
detector=FER()
a=detector.detect_emotions(img)
print(a)