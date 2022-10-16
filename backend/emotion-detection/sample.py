import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

img = cv2.imread('sample.png')

result = DeepFace.analyze(img,actions=['emotion'])

print(result)
