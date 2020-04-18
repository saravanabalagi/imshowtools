# imshowtools

![](https://img.shields.io/pypi/v/imshowtools)
![](https://img.shields.io/pypi/wheel/imshowtools)
![](https://img.shields.io/pypi/l/imshowtools)

This library lets you view images in Jupyter notebooks in a much simpler and intuitive way. Ships with a better 'imshow' function with Multi Images, Smart Wrap and BGR support!.

## Installation

To install `imshowtools`, simply do

```py
pip install imshowtools
```

## Quick Plot

Import `imshow` from `imshowtools` and use it:

```py
from imshowtools import imshow
import tensorflow as tf
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

imshow(x_train[0])
imshow(x_train[0], x_train[1], x_train[2])
imshow(*x_train[:20], cmap='binary')
imshow(*x_train[:100], cmap='binary', size=(10, 10))
```

You can use any matplotlib compatible `cmap`

![mnist](https://github.com/saravanabalagi/imshowtools/raw/master/example/mnist_intro.png)

Example [ipynb](https://github.com/saravanabalagi/imshowtools/blob/master/example/example.ipynb) notebook and [Python](https://github.com/saravanabalagi/imshowtools/blob/master/example/example.py) along with test images
provided in the example folder.

## Get Numpy Image

You can use obtain numpy image in any of `['RGB', 'RGBA', 'ARGB', 'BW', 'L', "BGR", "BGRA", "ABGR"]` colorspaces.

```py
image = imshow(*x_train[:100], return_image=True)
image = imshow(*x_train[:100], return_image="RGBA")
image = imshow(*x_train[:100], return_image="RGB")
image = imshow(*x_train[:100], return_image="BW")
print(image.shape)

# cv2.imwrite("saved_sample.png", image)
# do stuff with 'image' or even
# imshow(image)
```

Output:
```py
(288, 432, 3)
(288, 432, 4)
(288, 432, 3)
(288, 432)
```

## Rows and Columns

```py
imshow(*x_train[:15], cmap='Purples', rows=1)
imshow(*x_train[:24], cmap='Greens', columns=4)
```

![mnist](https://github.com/saravanabalagi/imshowtools/raw/master/example/mnist_rc.png)

## Open CV Images

```py
lenna = cv2.imread('example/lenna.png')
imshow(lenna)
cvshow(lenna)
imshow(lenna, mode='BGR')

image = imshow(*[lenna for _ in range(12)], return_image="BW")
print(image.shape)
imshow(image)
```
![lenna](https://github.com/saravanabalagi/imshowtools/raw/master/example/lenna_collage.png)

## Namespaces
If you do not want to use `imshow` directly in your app (maybe you have another function named imshow), you shall use it like

```py
import imshowtools
imshowtools.imshow(your_image)
```

or if you like to use a custom namespace
```py
import imshowtools as my_namespace
my_namespace.imshow(your_image)
```

## Contributing

Pull requests are very welcome.

1. Fork the repo
1. Create new branch with feature name as branch name
1. Check if things work with a jupyter notebook
1. Raise a pull request

## Licence

Please see attached [Licence](LICENCE)
