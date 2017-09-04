from setuptools import setup, find_packages

setup(
    name='segment',
    version='0.0.1',
    description='tool to record videos from Kodi on the command line or from within Kodi',
    author='NapoleonWils0n',
    url='https://github.com/NapoleonWils0n/segment',
    keywords=['ffmpeg', 'rtmpdump', 'kodi'],
    long_description='long description goes here',
    license='GPL',
    packages=find_packages(),
    zip_safe=False,
    scripts=['segemnt/segment']
)
