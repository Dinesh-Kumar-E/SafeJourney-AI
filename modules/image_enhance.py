import cv2
import numpy as np

image_path = r"D:\Dinesh-Kumar\Downloads\s0001_02343_0_0_1_0_0_01.png"  # Replace with the path to your image
img = cv2.imread(image_path)


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced_img = clahe.apply(gray_img)


alpha = 1.5
beta = 30 
enhanced_img = cv2.convertScaleAbs(enhanced_img, alpha=alpha, beta=beta)


cv2.imshow('Original Image', gray_img)
cv2.imshow('Enhanced Image', enhanced_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
