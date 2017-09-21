#from setuptools import setup
from distutils.core import setup

setup(
    name='pilfer',
    version='1.0',
    description='pilfer command line tool to record videos from Kodi',
    url='https://github.com/NapoleonWils0n/pilfer',
    author='NapoleonWils0n',
    maintainer='NapoleonWils0n',
    license='GPL',
    keywords='ffmpeg rtmpdump kodi',
    packages=['pilfer'],
    scripts=['pilfer/pilfer'],
    zip_safe=False
)
