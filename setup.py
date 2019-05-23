# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


setup(
    name='both',
    version='0.1.0',
    author='Grant Bakker',
    author_email='grant@bakker.pw',
    description='Python compatibility layer',
    url='https://bakkerthehacker.github.io/both/',
    classifiers=(
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ),
    packages=find_packages(exclude=['tests.*', 'tests']),
    install_requires=['six', 'source-transform>=0.1.1', 'future'],
)
