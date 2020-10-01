# -*- coding: utf-8 -*-
from os.path import join, dirname
import setuptools

with open(join(dirname(__file__), 'README.md')) as fhdl:
    long_description = fhdl.read().strip()

setuptools.setup(
    name='PiPyADC-py3',
    description="PiPyADC for python3",
    license="GPL",
    url="https://github.com/kizniche/PiPyADC-py3",
    download_url="https://github.com/kizniche/PiPyADC-py3",
    long_description=long_description,
    version='1.2',
    author="Kyle Gabriel",
    zip_safe=False,
    keywords=['PIPYADC-PY3'],
    classifiers=[
        "License :: OSI Approved :: GPL License",
        "Operating System :: POSIX :: Linux",
        'Programming Language :: Python',
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.5',
    packages=["pipyadc_py3"],
)
