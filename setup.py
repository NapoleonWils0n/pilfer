from setuptools import setup, find_packages

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pilfer',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',

    description='pilfer command line tool to record videos from Kodi',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/NapoleonWils0n/pilfer',

    # Author details
    author='NapoleonWils0n',
    author_email='',

    # Choose your license
    license='GPL',

    # What does your project relate to?
    keywords='sample setuptools development',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'pilfer=pilfer:main',
        ],
},
)