import warnings

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
        return img

    mode = mode.upper()
    if mode not in _SUPPORTED_MODES:
        raise ValueError('Mode {} not found. Use one from {}'.format(mode, _SUPPORTED_MODES))

    if _has_one_channel(img):
        mode = 'RGB'

    if mode == 'RGB':
        return img
    elif mode == 'BGR':
        if not _has_three_or_four_channels(img):
            warnings.warn(f'Image {index if index else ""} has {img.shape[2]} channels, expecting 3 or 4 channels.\n'
                          f'Using BGR mode may not produce expected output as it simply reverses channel order.')
        return img[:, :, ::-1]
