#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from coadlib import __author__, __version__, __doc__

with open("LICENSE", "r") as fp:
    license_message = fp.read()

setup(
    name="coadlib",
    author=__author__,
    description=__doc__.splitlines()[0],
    version=__version__,
    license=license_message,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Japanese",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Utilities"
    ]
)
