from setuptools import setup

setup(
    name='trdg',
    version='2.0',
    packages=['trdg', 'trdg.generators'],
    url='https://github.com/voun7/TextRecognitionDataGenerator',
    license='MIT',
    author='Victor N',
    author_email='',
    description="TextRecognitionDataGenerator: A synthetic data generator for text recognition",
    package_data={'trdg': ['**/*.txt', '**/*.ttf', '**/*.jpg'], },
    install_requires=[
        "pillow>=10.4.0",
        "opencv-python>=4.10.0.84",
        "tqdm>=4.66.5",
    ],
    entry_points={"console_scripts": ["trdg=trdg.run:main"]},
)
