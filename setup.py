#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import taggit_widgets

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = taggit_widgets.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-taggit-widgets',
    version=version,
    description="""Alternate widgets for django-taggit""",
    long_description=readme + '\n\n' + history,
    author='Ben Lopatin',
    author_email='ben@wellfire.co',
    url='https://github.com/bennylope/django-taggit-widgets',
    packages=[
        'taggit_widgets',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.4',
        'django-taggit',
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-taggit-widgets',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
