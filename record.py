#!/usr/bin/env python3 

import shlex
import pipes
from subprocess import check_call

# record function
def ffmpeg(url, options=None, tflag=None, duration=None):
    recordingfile = 'recordingfile' 
    ffcmd = "ffmpeg -hide_banner -stats -v panic '{1}' -i {0} -c:v copy -c:a copy {2} {3} {4}".format(url, options, tflag, duration, recordingfile)

    print(shlex.split(ffcmd))

