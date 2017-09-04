import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup




setup(
    name='pilfer',
    version='0.0.1',
    description='tool to record videos from Kodi on the command line or from within Kodi',
    author='NapoleonWils0n',
    url='https://github.com/NapoleonWils0n/pilfer',
    keywords=['ffmpeg', 'rtmpdump', 'kodi'],
    long_description='long description goes here',
    license='GPL',
    packages=['pilfer'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pilfer = pilfer:__main__'
        ]
    }
)
