#!/usr/bin/env python3

from setuptools import setup, find_packages
import pathlib

longDescription = (pathlib.Path(__file__).parent.resolve() / "README.md").read_text(encoding="utf-8")
installRequires = (pathlib.Path(__file__).parent.resolve() / "requirements.txt").read_text(encoding="utf-8").splitlines()

setup(
    name="svg2canvas",
    version="0.1.0",
    description="Convert your svg to code ",
    long_description=longDescription,
    url="https://github.com/olkiz/svg2canvas",
    author="olkiz",
    license='MIT',
    packages=['svg2canvas'] + find_packages(),
    python_requires=">=3.5, <4",
    zip_safe=False,
    install_requires=[installRequires],
    include_package_data=True,
    entry_points = {
        'console_scripts': [
            'svg2canvas = svg2canvas.svg2canvas:main'
        ]
    },
    classifiers=[
           "Programming Language :: Python :: 3",
           "License :: OSI Approved :: MIT License",
           "Operating System :: OS Independent",
    ]
)