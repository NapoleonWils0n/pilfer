#!/usr/bin/env python3 

import shlex
import pipes
from subprocess import check_call

def ffmpeg(**kwargs):
    recordingfile = 'recordingfile' 
    
    # get the values from the dictionary passed to the function
    values = list(kwargs.values())
    # url from kwargs which is the dictionary passed to the function
    url = kwargs['url']
    # dict minus first time which is the url, and minus the last 2 items tflag and duration
    options = values[1:]
    options_join = ' '.join(options)
    
    if 'duration' in kwargs:
        tflag = kwargs['tflag']
        duration = kwargs['duration']
        options = values[1:-2]
        options_join = ' '.join(options)
        print(tflag)
        print(duration)
    
    print(url)
    print(repr(options_join))


    #ffcmd = "ffmpeg -hide_banner -stats -v panic -i {url} -c:v copy -c:a copy".format(url)
    #ffcmd = "ffmpeg -hide_banner -stats -v panic {1} -i {0} -c:v copy -c:a copy {2} {3} {4}".format(url, options, tflag, duration, recordingfile)
    
    #print(ffcmd)
    #print(shlex.split(ffcmd))
