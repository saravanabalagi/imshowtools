# Version of imshowtools
__version__ = "0.2.0"


import numpy as np
from matplotlib import pyplot as plt

BGR_ERROR = 'BGR format could not be parsed'
BGR_ERROR_REASON = ': img should have 3 channels and format should be "hwc" and not "cwh"'
SUPPORTED_MODES = ['RGB', 'BGR']
def imshow(*images, cmap='viridis', rows=None, columns=None, mode='RGB'):
    """
    Shows image loaded by opencv after inverting the order of channels
    Can also be used to show single layer depth image
    Args:
        *images: one of more np.array of shape h,w,c or simple h,w
        cmap: specify a cmap to apply to all images (viridis by default)
        mode: specify a mode or color space RGB or BGR
        rows: number of rows to show
        columns: numbers of columns to show
    Returns:
        None
    """
    plt.rcParams['image.cmap'] = cmap
    mode = mode.upper()
    if mode not in SUPPORTED_MODES:
        print('Mode {} not found. Use one from {}'.format(mode, SUPPORTED_MODES))
        return

    no_of_images = len(images)
    if no_of_images is 0:
        print("Please provide atleast one image to display! Try again")
        return

    if no_of_images is 1:
        img = images[0]
        if mode == 'RGB': plt.imshow(img)
        elif mode == 'BGR':
            if is_bgr(img): plt.imshow(img[:,:,::-1])
            else: 
                print('{} for the image{}'.format(BGR_ERROR, BGR_ERROR_REASON))
                return
        plt.axis('off')
        return

    if rows is None: rows = int(np.sqrt(no_of_images))
    if columns is None: columns = int(np.ceil(no_of_images / rows))

    fig, axes = plt.subplots(rows, columns)
    for index, axis in enumerate(axes.reshape(-1)):
        if index < no_of_images:
            img = images[index]
            if mode == 'RGB': 
                axis.imshow(img)
            elif mode == 'BGR': 
                if is_bgr(img): axis.imshow(img[:,:,::-1])
                else: print('{} for image #{}{}'.format(BGR_ERROR, index, BGR_ERROR_REASON))
        axis.axis('off')

def is_bgr(img):
    if len(img.shape)==3 and img.shape[2]==3:
        return True
    return False