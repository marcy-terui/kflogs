#!/usr/bin/env python

import os
import kflogs

from setuptools import setup, find_packages

description = 'Amazon Kinesis Firehose logging handler and utilities'
long_description = description
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

setup_options = dict(
    name='kflogs',
    version=kflogs.__version__,
    description=description,
    long_description=long_description,
    author='Masashi Terui',
    author_email='marcy9114+pypi@gmail.com',
    url='https://github.com/marcy-terui/kflogs',
    packages=find_packages(exclude=['tests*', 'test', 'register']),
    install_requires=[
        'boto3'
    ],
    license="MIT License",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords='aws kinesis firehose logging',
)

setup(**setup_options)
