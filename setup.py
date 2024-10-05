# Always prefer setuptools over distutils
# To use a consistent encoding
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="trdg",
    version="2.0",
    description="TextRecognitionDataGenerator: A synthetic data generator for text recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/voun7/TextRecognitionDataGenerator",
    author="Victor N",
    author_email="",
    license="MIT",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    include_package_data=True,
    install_requires=[
        "pillow>=10.4.0",
        "opencv-python>=4.10.0.84",
        "tqdm>=4.66.5",
    ],
    entry_points={
        "console_scripts": [
            "trdg=trdg.run:main"
        ],
    },
)
