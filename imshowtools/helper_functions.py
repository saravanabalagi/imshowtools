_SUPPORTED_MODES = ['RGB', 'BGR']


def _has_three_channels(img):
    if len(img.shape) == 3 and img.shape[2] == 3:
        return True
    return False


def _convert_mode(img, mode=None, index=None):
    if mode is None:
        return img

    mode = mode.upper()
    if mode not in _SUPPORTED_MODES:
        raise ValueError('Mode {} not found. Use one from {}'.format(mode, _SUPPORTED_MODES))
    if not _has_three_channels(img):
        raise ValueError(f'Image {index if index else ""} does not have 3 channels, '
                         f'but requiring to output in {mode} mode')

    if mode == 'RGB':
        return img
    elif mode == 'BGR':
        return img[:, :, ::-1]
