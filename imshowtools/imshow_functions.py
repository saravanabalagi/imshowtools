from matplotlib import pyplot as plt
from typing import Union, Any, List
import math

from imshowtools.helper_functions import _convert_mode, _SUPPORTED_MODES, _imshow_finally, _RETURN_IMAGE_TYPES
from imshowtools.validation_functions import _validate_list


def imshow(*images, cmap: Union[str, List, None] = None, rows: int = None, columns: int = None,
           mode: Union[str, List] = None, window_title: str = None, title: Union[str, List] = None,
           return_image: Union[bool, str] = False) -> Union[None, Any]:
    """
    Shows image loaded by opencv after inverting the order of channels
    Can also be used to show single layer depth image
    Args:
        *images: one of more np.array of shape h,w,c or simple h,w
        cmap: specify a cmap to apply to all images (gray by default)
        mode: specify a mode or color space one in RGB or BGR
        rows: number of rows to show
        columns: numbers of columns to show
        window_title: window title (not applicable for ipynb notebooks)
        title: title for the image, or list of titles, one for each image
        return_image: if one of ['RGB', 'RGBA', 'ARGB', 'BW', 'L', "BGR", "BGRA", "ABGR"] returns Image.
                      if True returns 'RGB'. Does not display image if set. if False, returns None, but displays image.
    Returns:
        None if return_image is False, else uint8 numpy.ndarray of shape [h,w,c] or [h,w] depending on its value.
    """
    num_images = len(images)
    if num_images is 0:
        print("Please provide at least one image to display! Try again")
        return

    # Setting fig in other cases works,
    # But matplotlib will print a warning
    # <Figure size 432x288 with 0 Axes>
    fig = None
    if window_title is not None or return_image is True or return_image in _RETURN_IMAGE_TYPES:
        fig = plt.figure(window_title)

    _validate_list(mode, [str, type(None)], num_images=num_images, list_name='mode', in_str=_SUPPORTED_MODES)
    _validate_list(cmap, [str, type(None)], num_images=num_images, list_name='cmap', in_str=plt.colormaps())
    _validate_list(title, [str, type(None)], num_images=num_images, list_name='title')

    if type(title) is str:
        plt.title(title)

    if num_images is 1:
        img = images[0]
        img = _convert_mode(img, mode, cmap)
        plt.imshow(img)
        plt.axis('off')
        return _imshow_finally(fig, return_image)

    if rows is None:
        if columns is not None:
            rows = int(math.ceil(num_images / columns))
        else:
            rows = int(math.sqrt(num_images))
    if columns is None:
        columns = int(math.ceil(num_images / rows))

    fig, axes = plt.subplots(rows, columns)
    for index, axis in enumerate(axes.reshape(-1)):
        if index < num_images:
            img = images[index]
            current_mode = mode[index] if type(mode) is list else mode
            current_cmap = cmap[index] if type(cmap) is list else cmap
            current_title = title[index] if type(title) is list else title
            img = _convert_mode(img, current_mode, current_cmap, index=index)
            if current_title is not None:
                axis.set_title(current_title)
            axis.imshow(img, cmap=current_cmap)
        axis.axis('off')

    return _imshow_finally(fig, return_image)


def cvshow(*images, cmap: str = 'gray', rows: int = None, columns: int = None, window_title: str = None,
           title: Union[str, List] = None, return_image: Union[bool, str] = False) -> Union[None, Any]:
    """
    Convenience function for displaying images loaded by OpenCV which are read as BGR by default,
    same as using imshow with `mode='BGR'`
    Args:
        *images: one of more np.array of shape h,w,c or simple h,w
        cmap: specify a cmap to apply to all images (gray by default)
        rows: number of rows to show
        columns: numbers of columns to show
        window_title: window title (not applicable for ipynb notebooks)
        title: title for the image, or list of titles - one for each image
        return_image: if one of ['RGB', 'RGBA', 'ARGB', 'BW', 'L', "BGR", "BGRA", "ABGR"] returns Image.
                      if True returns 'RGB'. Does not display image if set. if False, returns None, but displays image.
    Returns:
        None if return_image is False, else uint8 numpy.ndarray of shape [h,w,c] or [h,w] depending on its value.
    """
    return imshow(*images, cmap=cmap, rows=rows, columns=columns, mode='BGR',
                  window_title=window_title, title=title, return_image=return_image)
