#!/usr/bin/env python

"""
setuptools install script.
"""
import os
import re

from setuptools import setup, find_packages

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')

requires = [
        'datacoco==0.1'
        'pyyaml==3.13',
        'slackclient==1.3.0',
        'redis==2.10.6',
        'json2html==1.0.0',
        'pytest==4.0.1'
]

setup(
    name="hambot",
    version=VERSION,
    author="Equinox",
    description="",
    long_description=open("README.rst").read(),
    url="https://github.com/equinoxfitness/hambot",
    scripts=[],
    license="TBD",
    packages=find_packages(exclude=["tests*"]),
    install_requires=requires,
    classifiers=[
        'Development Status :: 1 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ]
)
