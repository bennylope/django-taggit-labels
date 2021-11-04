#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import taggit_labels

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = taggit_labels.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-taggit-labels',
    version=version,
    description="""Alternate labels for django-taggit""",
    long_description=readme + '\n\n' + history,
    author='Ben Lopatin',
    author_email='ben@wellfire.co',
    url='https://github.com/bennylope/django-taggit-labels',
    packages=[
        'taggit_labels',
    ],
    include_package_data=True,
    install_requires=[
        'django-taggit>=0.17.0',
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-taggit-labels',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Development Status :: 5 - Production/Stable',
    ],
)
