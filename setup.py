# -*- coding: UTF-8 -*-

from os.path import dirname
import sys

import setuptools
from distutils.core import setup

import re

VERSIONFILE = 'term2048/__init__.py'
verstrline = open(VERSIONFILE, 'rt').read()
VSRE = r'^__version__\s+=\s+[\'"]([^\'"]+)[\'"]'
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % VERSIONFILE)

setup(
    name='terminal2048',
    version=verstr,
    author='MSJX',
    author_email='mr.msjx@foxmail.com',
    packages=['term2048'],
    url='https://github.com/MSJX/terminal2048',
    description='2048 in your terminal',
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='2048 terminal',
    entry_points={
        'console_scripts': [
            'terminal2048 = term2048.ui:start_game'
        ]
    },
)