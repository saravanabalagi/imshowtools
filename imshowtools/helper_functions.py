import warnings
import platform
import tempfile
from datetime import datetime
import os

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread

_SUPPORTED_MODES = ['RGB', 'BGR']


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


def _convert_mode(img, mode=None, index=None):
    if mode is None:
        mode = 'RGB'

    if img is None:
        raise ValueError(f'Image{(" " + index) if index else ""} is None')

    mode = mode.upper()
    if mode not in _SUPPORTED_MODES:
        raise ValueError('Mode {} not found. Use one from {}'.format(mode, _SUPPORTED_MODES))

    if _has_one_channel(img):
        # squeeze if it has shape [h, w, 1]
        if len(img.shape) == 3:
            img = img[:, :, 0]

        # Colorspace conversion not required
        # for single channel images
        mode = 'RGB'

    if mode == 'RGB':
        return img
    elif mode == 'BGR':
        if not _has_three_or_four_channels(img):
            warnings.warn(f'Image {index if index else ""} has {img.shape[2]} channels, expecting 3 or 4 channels.\n'
                          f'Using BGR mode may not produce expected output as it simply reverses channel order.')
        return img[:, :, ::-1]


def _imshow_finally(fig, return_image):
    if not return_image:
        plt.show()
        return
    else:
        # workaround for not using numpy, uses disk, slower
        # return _save_and_retrieve_image()

        # direct method, not using disk
        fig.canvas.draw()
        width, height = fig.get_size_inches() * fig.get_dpi()
        image = np.frombuffer(fig.canvas.tostring_argb(), dtype='uint8').reshape(int(height), int(width), 4)
        image = image[:, :, [1, 2, 3, 0]]          # convert from argb to rgba
        plt.close(fig)
        return image


def _save_and_retrieve_image():
    tempdir = '/tmp' if platform.system() == 'Darwin' else tempfile.gettempdir()
    filename = f'{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
    filepath = os.path.join(tempdir, filename)
    plt.savefig(filepath, transparent=True)

    image = imread(filepath)
    os.remove(filepath)
    return image
