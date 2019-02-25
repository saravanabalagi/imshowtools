# imshowtools

This library that allows you to view images in Jupyter notebooks in a much simpler way.

## Installation

To install imshowtools,

```python
pip install imshowtools
```

## Usage

Open a jupyter notebook and use imshowtools as shown below:

### Show a Single Image

To show a single image
```python
from imshowtools import *
imshow(your_image)
```

### Show Multiple Images

To show multiple images
```python
from imshowtools import *
imshow(image_1, image_2, image_3)
```

### Show Multiple Images from Array
```python
from imshowtools import *
imshow(*my_image_array)
```

### Namespaces
If you do not want to use `imshow` directly in your app (maybe you have another function named imshow), you shall use it like

```python
import imshowtools
imshowtools.imshow(your_image)
```

## Uninstall

To uninstall `imshowtools`,

```python
pip uninstall imshowtools
```

## Licence

MIT License

Copyright (c) 2019 Saravanabalagi Ramachandran

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.