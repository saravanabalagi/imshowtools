def _validate_list(values, types, list_name, num_images, in_str=None):

    type_error_msg = f'{list_name} should either be one of {[t.__name__ for t in types]} or a list of the same\n'
    value_error_msg = f'If {list_name} contains a string it should be one of {in_str}\n'

    if num_images is 1 and type(values) is list:
        raise TypeError(f'Cannot process a list of {list_name} for a single image')
    elif num_images > 1 and type(values) is list:
        if len(values) is not num_images:
            raise ValueError(f'Given {len(values)} {list_name} values for {num_images} images. Expected {num_images}')
        for value in values:
            if type(value) not in types:
                raise TypeError(type_error_msg + f'Given {type(value).__name__}')
            if type(value) is str and in_str is not None:
                if value not in in_str:
                    raise ValueError(value_error_msg + f'Given {value}')
        return
    elif type(values) in types:
        return
    raise TypeError(type_error_msg + f'Given {type(values)}')
