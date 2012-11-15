#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

from octokitten import __version__, __description__

setup(
    name='octokitten',
    version=__version__,
    author='Shane R. Spencer',
    author_email='shane@bogomip.com',
    packages=['octokitten'],
    url='https://github.com/whardier/octokitten',
    license='MIT',
    description=__description__,
    long_description=open('README').read(),
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ],
    entry_points={
        'console_scripts': [
            'octokitten = octokitten.__init__:run',
        ],
    }

)


