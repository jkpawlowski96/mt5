import setuptools


import platform
system = platform.system()

if system == 'Windows':
    from linux import *
else:
    pass


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mt5", # Replace with your own username
    version="0.0.2.1",
    author="Jakub Pawłowski",
    author_email="jkpawlowski96@gmail.com",
    description="MetaTrader5 multiplatform python api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jkpawlowski96/mt5",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)