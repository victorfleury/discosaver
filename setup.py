#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Victor Fleury",
    python_requires='>=3.5',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
    description="A simple tool to automatically save the Discover Weekly playlist in spotify",
    entry_points={
        'console_scripts': [
            'discosaver=discosaver.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='discosaver',
    name='discosaver',
    packages=find_packages(include=['discosaver', 'discosaver.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/victorfleury/discosaver',
    version='0.1.0',
    zip_safe=False,
)
