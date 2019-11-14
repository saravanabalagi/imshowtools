from imshowtools.imshow_functions import imshow
import cv2

image = cv2.imread("lenna.png")
imshow(image, mode='BGR', title="Lenna")

image = cv2.imread("mnist_100.png")
imshow(image, cmap='gray')
