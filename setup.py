#!/usr/bin/env python3

from distutils.core import setup

setup(
    name = "segment",
    packages = ["segment"],
    entry_points={
          'console_scripts': [
              'segment = segment.__main__:main'
          ]
    },
    version = "1.0",
    description = "tool to record videos from Kodi on the command line or from within Kodi",
    author = "NapoleonWils0n",
    url = "",
    keywords = ["ffmpeg", "rtmpdump", "kodi"],
    long_description = ""
)
