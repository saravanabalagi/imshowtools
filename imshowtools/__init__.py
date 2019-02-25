# Version of imshowtools
__version__ = "0.1.0"


import numpy as np
from matplotlib import pyplot as plt

def imshow(*images, cmap='viridis'):
    """
    Shows image loaded by opencv after inverting the order of channels
    Can also be used to show single layer depth image
    Args:
        *images: one of more np.array of shape h,w,c or simple h,w
        cmap: specify a cmap to apply to all images (viridis by default)
    Returns:
        None
    """
    plt.rcParams['image.cmap'] = cmap

    no_of_images = len(images)
    if no_of_images is 0:
        print("Please provide atleast one image to display! Try again")
        return

    if no_of_images is 1:
        plt.imshow(images[0])
        plt.axis('off')
        return

    rows = int(np.sqrt(no_of_images))
    columns = int(np.ceil(no_of_images / rows))

    fig, axes = plt.subplots(rows, columns)
    for index, axis in enumerate(axes.reshape(-1)):
        if index < no_of_images:
            axis.imshow(images[index])
        axis.axis('off')


def imshowline(*images, cmap='viridis'):
    """
    Shows image loaded by opencv after inverting the order of channels
    Can also be used to show single layer depth image
    Args:
        *images: one of more np.array of shape h,w,c or simple h,w
        cmap: specify a cmap to apply to all images (jet by default)
    Returns:
        None
    """
    plt.rcParams['image.cmap'] = cmap

    no_of_images = len(images)
    if no_of_images is 0:
        print("Please provide atleast one image to display! Try again")
        return

    if no_of_images is 1:
        plt.imshow(images[0])
        plt.axis('off')
        return

    rows = 1
    columns = int(np.ceil(no_of_images / rows))

    fig, axes = plt.subplots(rows, columns)
    for index, axis in enumerate(axes.reshape(-1)):
        if index < no_of_images:
            axis.imshow(images[index])
        axis.axis('off')