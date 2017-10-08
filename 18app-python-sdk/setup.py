#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'zeep',
    'requests',
    'lxml'
]

setup_requirements = [
    # TODO(italia): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'mock'
]

setup(
    name='python_18app',
    version='0.1.0',
    description="Merchant SDK for 18App - Python",
    long_description=readme + '\n\n' + history,
    author="Developers Italia",
    author_email='info@developers.italia.it',
    url='https://github.com/italia/python_18app',
    packages=find_packages(include=['python_18app']),
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='python_18app',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
