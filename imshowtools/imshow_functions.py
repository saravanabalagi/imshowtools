from matplotlib import pyplot as plt
from typing import Union, Any
import math

from imshowtools.helper_functions import _convert_mode, _SUPPORTED_MODES, _imshow_finally
from imshowtools.validation_functions import _validate_list


def imshow(*images, cmap: Union[str, list, None] = None, rows: int = None, columns: int = None,
           size: Union[tuple, list] = None, padding: Union[bool, float, int, tuple, list] = False,
           mode: Union[str, list] = 'RGB', window_title: str = None, title: Union[str, list, None] = None,
           return_image: Union[bool, str] = False) -> Union[None, Any]:
    """
    Shows image loaded by opencv after inverting the order of channels
    Can also be used to show single layer depth image
    Args:
        *images: one of more np.array of shape h,w,c or simple h,w
        cmap: specify a cmap to apply to all images, applicable only for single channel image, defaults to None
        mode: specify a mode or color space one in RGB or BGR, applicable only for 3 or 4 channel image
        rows: number of rows to show
        columns: numbers of columns to show
        size: size of the figure in inches in order [w,h] as tuple or list
        padding: amount of padding as a fraction of the font size.
                 Shall also be given as a list with params for tight_layout() function
        window_title: window title (not applicable for ipynb notebooks)
        title: title for the image, or list of titles, one for each image
        return_image: if one of ['RGB', 'RGBA', 'ARGB', 'BW', 'L', 'BGR', 'BGRA', 'ABGR'] returns Image.
                      if True returns 'RGB'. Does not display image if set. if False, returns None, but displays image.
    Returns:
        None if return_image is False, else uint8 numpy.ndarray of shape [h,w,c] or [h,w] depending on its value.
    """
    num_images = len(images)
    if num_images is 0:
        print("Please provide at least one image to display! Try again")
        return

    _validate_list(mode, [str], num_images=num_images, list_name='mode', in_str=_SUPPORTED_MODES)
    _validate_list(cmap, [str, type(None)], num_images=num_images, list_name='cmap', in_str=plt.colormaps())
    _validate_list(title, [str, type(None)], num_images=num_images, list_name='title')

    if num_images is 1:
        img = images[0]
        img = _convert_mode(img, mode, cmap)
        plt.imshow(img, cmap=cmap)
        plt.axis('off')
        fig = plt.gcf()
        return _imshow_finally(fig, return_image, window_title=window_title,
                               plt_title=title, padding=padding, size=size)

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
            current_title = title[index] if type(title) is list else None
            img = _convert_mode(img, current_mode, current_cmap, index=index)
            if current_title is not None:
                axis.set_title(current_title)
            axis.imshow(img, cmap=current_cmap)
        axis.axis('off')

    return _imshow_finally(fig, return_image, window_title=window_title,
                           plt_title=title, padding=padding, size=size)


def cvshow(*images, cmap: Union[str, list, None] = None, rows: int = None, columns: int = None,
           size: Union[tuple, list] = None, padding: Union[bool, float, int, tuple, list] = True,
           window_title: str = None, title: Union[str, list] = None,
           return_image: Union[bool, str] = False) -> Union[None, Any]:
    """
    Shows image loaded by opencv after inverting the order of channels
    Can also be used to show single layer depth image
    Args:
        *images: one of more np.array of shape h,w,c or simple h,w
        cmap: specify a cmap to apply to all images, applicable only for single channel image, defaults to None
        rows: number of rows to show
        columns: numbers of columns to show
        size: size of the figure in inches in order [w,h] as tuple or list
        padding: amount of padding as a fraction of the font size.
                 Shall also be given as a list with params for tight_layout() function
        window_title: window title (not applicable for ipynb notebooks)
        title: title for the image, or list of titles, one for each image
        return_image: if one of ['RGB', 'RGBA', 'ARGB', 'BW', 'L', 'BGR', 'BGRA', 'ABGR'] returns Image.
                      if True returns 'RGB'. Does not display image if set. if False, returns None, but displays image.
    Returns:
        None if return_image is False, else uint8 numpy.ndarray of shape [h,w,c] or [h,w] depending on its value.
    """
    return imshow(*images, cmap=cmap, rows=rows, columns=columns, size=size, padding=padding, mode='BGR',
                  window_title=window_title, title=title, return_image=return_image)
