from matplotlib import pyplot as plt
from typing import Union
import math

from imshowtools.helper_functions import _convert_mode, _SUPPORTED_MODES


def imshow(*images, cmap: str = 'viridis', rows: int = None, columns: int = None,
           mode: Union[str, list] = None, window_title: str = None, title: Union[str, list] = None) -> None:
    """
    Shows image loaded by opencv after inverting the order of channels
    Can also be used to show single layer depth image
    Args:
        *images: one of more np.array of shape h,w,c or simple h,w
        cmap: specify a cmap to apply to all images (viridis by default)
        mode: specify a mode or color space one in RGB or BGR
        rows: number of rows to show
        columns: numbers of columns to show
        window_title: window title (not applicable for ipynb notebooks)
        title: title for the image, or list of titles - one for each image
    Returns:
        None
    """
    plt.rcParams['image.cmap'] = cmap
    if window_title is not None:
        plt.figure(window_title)

    title_list = None
    if type(title) is str:
        plt.title(title)
    elif type(title) is list:
        if len(title) == len(images) and all([type(el) == str for el in title]):
            title_list = title
        else:
            raise ValueError('Title can either be a string or a list of strings')

    mode_list = None
    if type(mode) is list:
        if len(mode) == len(images) and all([type(el) == str or el is None for el in mode]):
            mode_list = mode
        else:
            raise ValueError(f'Mode can either be a string or a list of strings from {_SUPPORTED_MODES}')

    no_of_images = len(images)
    if no_of_images is 0:
        print("Please provide atleast one image to display! Try again")
        return

    if no_of_images is 1:
        img = images[0]
        img = _convert_mode(img, mode)
        plt.imshow(img)
        plt.axis('off')
        plt.show()
        return

    if rows is None:
        rows = int(math.sqrt(no_of_images))
    if columns is None:
        columns = int(math.ceil(no_of_images / rows))

    fig, axes = plt.subplots(rows, columns)
    for index, axis in enumerate(axes.reshape(-1)):
        if index < no_of_images:
            img = images[index]
            if mode_list:
                img = _convert_mode(img, mode_list[index], index)
            else:
                img = _convert_mode(img, mode, index)
            if title_list:
                axis.set_title(title_list[index])
            axis.imshow(img)
        axis.axis('off')

    plt.show()
    return
