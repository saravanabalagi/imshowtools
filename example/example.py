from imshowtools import imshow
import cv2


if __name__ == '__main__':

    image_lenna = cv2.imread("lenna.png")
    imshow(image_lenna, mode='BGR', window_title="Lenna")

    image_lenna_bgr = cv2.imread("lenna_bgr.png")
    imshow(image_lenna, image_lenna_bgr, cmap='gray', mode=['BGR', None], title=['lenna_rgb', 'lenna_bgr'])
