import warnings

import numpy as np
from matplotlib import pyplot as plt

_SUPPORTED_MODES = ['RGB', 'BGR']
_RETURN_IMAGE_TYPES = ['RGB', 'RGBA', 'ARGB', 'BW', 'L', "BGR", "BGRA", "ABGR"]


def _set_padding(fig, padding):
    if padding is True:
        fig.tight_layout()
    elif type(padding) in [float, int]:
        fig.tight_layout(pad=padding)

    # padding param can also be a list with each param corresponding to params of
    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.tight_layout.html
    elif type(padding) in [list, tuple]:
        if len(padding) == 1:
            fig.tight_layout(pad=padding[0])
        elif len(padding) == 2:
            fig.tight_layout(pad=padding[0], h_pad=padding[1], w_pad=padding[1])
        elif len(padding) == 3:
            fig.tight_layout(pad=padding[0], h_pad=padding[1], w_pad=padding[2])
        elif len(padding) == 4:
            fig.tight_layout(pad=padding[0], h_pad=padding[1], w_pad=padding[2], rect=padding[3])
        else:
            raise ValueError("Can only accept upto 4 args for padding")


def _set_window_plot_title(fig, window_title, plt_title):
    if window_title is not None and type(window_title) is str:
        fig.canvas.set_window_title(window_title)
    if plt_title is not None and type(plt_title) is str:
        # Refer to https://stackoverflow.com/a/55768955/3125070
        fig.subplots_adjust(top=0.9)
        fig.suptitle(plt_title, y=0.96)


def _has_one_channel(img):
    if len(img.shape) == 2:
        return True
    if len(img.shape) == 3 and img.shape[2] == 1:
        return True
    return False


def _has_three_or_four_channels(img):
    if len(img.shape) == 3 and img.shape[2] in [3, 4]:
        return True
    return False


def _convert_mode(img, mode=None, cmap=None, index=None):

    if img is None:
        image_index_str = "Image"
        if index is not None:
            image_index_str += " " + str(index)
        raise ValueError(f'{image_index_str} is None')

    mode = mode.upper()
    if mode not in _SUPPORTED_MODES:
        raise ValueError('Mode {} not found. Use one from {}'.format(mode, _SUPPORTED_MODES))

    if _has_one_channel(img):
        # squeeze if it has shape [h, w, 1]
        if len(img.shape) == 3:
            img = img[:, :, 0]

        # Convert 1 Channel to 3 Channel
        # if no cmap is applied
        if cmap is None:
            img = np.stack([img]*3, axis=-1)

    if mode == 'BGR':
        if not _has_three_or_four_channels(img):
            warnings.warn(f'Image {index if index else ""} has {img.shape[2]} channels, expecting 3 or 4 channels.\n'
                          f'Using BGR mode may not produce expected output as it simply reverses channel order.')
        return img[:, :, ::-1]

    return img


def _imshow_finally(fig, return_image, window_title, plt_title, padding, size):

    # Set Size
    if size is not None:
        fig.set_size_inches(size)

    # Set Plot Title, Window Title and Padding
    _set_padding(fig, padding=padding)
    _set_window_plot_title(fig, window_title, plt_title)

    # Show image when return_image is None or False
    if return_image is None or return_image is False:
        plt.show()
        return

    # If True or str, return appropriate image
    else:
        return_type = "RGB"
        if type(return_image) is bool and return_image is True:
            return_type = "RGB"
        elif type(return_image) is str and return_image in _RETURN_IMAGE_TYPES:
            return_type = return_image
        else:
            warnings.warn(f'`return_image` attribute has to either bool or one of {_RETURN_IMAGE_TYPES}\n'
                          f'Given return image: {return_image} of type {type(return_image).__name__}\n'
                          f'Returning the image with default type: {return_type}')

        fig.canvas.draw()
        width, height = fig.get_size_inches() * fig.get_dpi()
        image_argb = np.frombuffer(fig.canvas.tostring_argb(), dtype='uint8').reshape(int(height), int(width), 4)
        image_rgba = image_argb[:, :, [1, 2, 3, 0]]       # convert from argb to rgba
        plt.close(fig)

        if return_type == "RGB":
            return image_rgba[..., :3]
        elif return_type == "BGR":
            return image_rgba[..., [2, 1, 0]]
        elif return_type == "BGRA":
            return image_rgba[..., [2, 1, 0, 3]]
        elif return_type == "ABGR":
            return image_rgba[..., [3, 2, 1, 0]]
        elif return_type in ["BW", "L"]:
            # ITU-R 601-2 luma transform
            return np.dot(image_rgba[..., :3], [0.2989, 0.5870, 0.1140]).astype('uint8')
        elif return_type == "ARGB":
            return image_argb
        elif return_type == "RGBA":
            return image_rgba
        return image_rgba[..., :3]
