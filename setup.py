#!/usr/bin/env python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mansnip-kristopolous", 
    version="0.3.3",
    scripts=["mansnip"],
    author="Chris McKenzie",
    author_email="kristopolous@yahoo.com",
    description="Finding just the snippets in man page you care about",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kristopolous/mansnip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.2',
)
