from setuptools import setup

setup(
    name='pilfer',
    version='0.1',
    description='pilfer command line tool to record videos from Kodi',
    url='https://github.com/NapoleonWils0n/pilfer',
    author='NapoleonWils0n',
    author_email='',
    license='GPL',
    keywords='ffmpeg rtmpdump kodi',
    packages=['pilfer'],
    entry_points={
        'console_scripts': ['pilfer=pilfer.__main__:main'],
    },
    zip_safe=False
)
