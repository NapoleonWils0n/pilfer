#!/usr/bin/env python3

from distutils.core import setup, find_packages

setup(
    name='segment',
    packages=['segment'],
    version='0.0.1',
    description='tool to record videos from Kodi on the command line or from within Kodi',
    author='NapoleonWils0n',
    url='https://github.com/NapoleonWils0n/segment',
    keywords=['ffmpeg', 'rtmpdump', 'kodi'],
    long_description='long description goes here',
    license='GPL',
    packages=find_packages(),
    zip_safe=False,
    entry_points={
          'console_scripts': [
              'segment=segment:main'
          ]
    }

)
