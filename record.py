#!/usr/bin/env python3 

import shlex
import pipes
from subprocess import check_call

# record function
def ffmpeg(url, options=None, tflag=None, duration=None):
    recordingfile = 'recordingfile' 
    if options:
        ffcmd = "ffmpeg -hide_banner -stats -v panic '{1}' -i {0} -c:v copy -c:a copy {2}".format(url, options, recordingfile)
    else:
        ffcmd = "ffmpeg -hide_banner -stats -v panic -i {0} -c:v copy -c:a copy {1}".format(url, recordingfile)

    print(shlex.split(ffcmd))

