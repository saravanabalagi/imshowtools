from imshowtools import imshow
import cv2


if __name__ == '__main__':

    image_lenna = cv2.imread("lenna.png")
    imshow(image_lenna, mode='BGR', window_title="LennaWindow", title="Lenna")

    image_lenna_bgr = cv2.imread("lenna_bgr.png")
    imshow(image_lenna, image_lenna_bgr, mode=['BGR', 'RGB'], title=['lenna_rgb', 'lenna_bgr'])
    imshow(*[image_lenna for _ in range(12)], title=["Lenna" for _ in range(12)], window_title="LennaWindow")
    imshow(*[image_lenna for _ in range(30)], title="Lenna", padding=(1, 1, 0, (0, 0, 0.8, 0.8)))
