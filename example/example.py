from imshowtools import imshow
import cv2

image = cv2.imread("lenna.png")
imshow(image, mode='BGR')