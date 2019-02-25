import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="imshowtools",
    version="0.2.0",
    description="imshowtools contains simplified imshow functions to show multiple images and with other options",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/saravanabalagi/imshowtools",
    author="Saravanabalagi Ramachandran",
    author_email="saravanabalagi@hotmail.com",
    license="MIT",
    classifiers=[
    	"Development Status :: 3 - Alpha",
    	"Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["imshowtools"],
    include_package_data=True,
    install_requires=["numpy", "matplotlib"]
)