#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup
from sys import version


if version < '2.7':
    raise NotImplementedError("DateRanger requires Python 2.7.* or above.")


setup(
    name='DateRanger',
    url='https://github.com/spitfire-sidra/DateRanger',
    version='0.3.0.alpha',
    author='Amo Chen',
    author_email='spitfire.sidra@gmail.com',
    packages=['DateRanger',],
    license='License.txt',
    description='Useful business date ranges',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
