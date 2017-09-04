

from setuptools import setup

setup(name='pilfer',
      version='0.0.1',
      packages=['pilfer'],
      entry_points={
          'console_scripts': [
              'pilfer = pilfer.__main__:main'
          ]
      },
      )
