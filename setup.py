#!/usr/bin/env python3

from setuptools import find_packages, setup

import saveread

setup(
    packages=find_packages(exclude=['saveread.bin']),
    scripts=['saveread/bin/saveread'],
    name='saveread',
    version=saveread.__version__,
    author='M157q',
    author_email='M157q.tw@gmail.com',
    url="https://github.com/M157q/saveread",
    keywords="cli, web",
    description="Save what you've read",
    platforms=['Linux'],
    license='GPL3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ],
)
