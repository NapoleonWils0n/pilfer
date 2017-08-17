#!/usr/bin/env python3 

import shlex
import pipes
from subprocess import check_call

def ffmpeg(**kwargs):
    recordingfile = 'recordingfile' 
    
    print(kwargs)

#    v = list(kwargs.values())
#    urlslice = v[1:]
#    options = ' '.join(urlslice)

    #ffcmd = "ffmpeg -hide_banner -stats -v panic -i {url} -c:v copy -c:a copy".format(url)
    #ffcmd = "ffmpeg -hide_banner -stats -v panic {1} -i {0} -c:v copy -c:a copy {2} {3} {4}".format(url, options, tflag, duration, recordingfile)
    
    #print(ffcmd)

    #print(shlex.split(ffcmd))
