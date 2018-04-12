#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from os import path
from codecs import open  # To use a consistent encoding
from setuptools import setup, find_packages


HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name="cross2rekordbox_xml",
    version="2018.04a1",
    description="Tool to fix beatgrid offsets in rekordbox.xml exported by Mixvibes Cross.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/binaryguru/cross2rekordbox_xml',
    author="André Perron",
    author_email="binaryguruca@yahoo.ca",
    license="MIT License",
    # packages=["elementtree"],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    platforms="Python 2.7.14 and later.",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='utility',
    py_modules=["cross2rekordbox_xml"],
    install_requires=['elementtree'],
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/binaryguru/cross2rekordbox_xml/issues',
        'Source': 'https://github.com/binaryguru/cross2rekordbox_xml',
        'MIT License': 'https://spdx.org/licenses/MIT.html'
    },
)
