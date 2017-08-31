#!/usr/bin/env python3 

import shlex
import sys, os
import subprocess
from datetime import datetime 

def ffmpeg(**kwargs):
    home = os.path.expanduser('~')
    desktop = '/Desktop/'
    time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ext = '.mkv'
    recordingfile = home + desktop + 'video-' + time + ext
    
    # get the values from the dictionary passed to the function
    values = list(kwargs.values())
    # url from kwargs which is the dictionary passed to the function
    url = kwargs['url']

    ffcmd = "ffmpeg -hide_banner -stats -v panic -i {0} -c:v copy -c:a copy {1}".format(url, recordingfile)

    if 'user-agent' or 'referer' or 'cookie' in kwargs:
        # dict minus first time which is the url
        options = values[1:]
        remove_bracket = str(options)[1:-1]
        options_join = ''.join(remove_bracket).replace('"', '')
        ffcmd = "ffmpeg -hide_banner -stats -v panic {1} -i {0} -c:v copy -c:a copy {2}".format(url, options_join, recordingfile)
    
    if 'duration' in kwargs:
        tflag = kwargs['tflag']
        duration = kwargs['duration']
        # dict minus first time which is the url, and minus the last 2 items tflag and duration
        options = values[1:-2]
        remove_bracket = str(options)[1:-1]
        options_join = ''.join(remove_bracket).replace('"', '')
        ffcmd = "ffmpeg -hide_banner -stats -v panic {1} -i {0} -c:v copy -c:a copy {2} {3} {4}".format(url, options_join, tflag, duration, recordingfile)
    

    # split the ffmpeg command for subprocess
    ffsplit = shlex.split(ffcmd)

    print("running ffmpeg command:")
 
    # try ffmpeg function except keyboard interupt if user quits script with control c
    try:
        process = subprocess.run(ffsplit)
    except KeyboardInterrupt:
        print("recording stopped by user")


def rtmp(**kwargs):
    home = os.path.expanduser('~')
    desktop = '/Desktop/'
    time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ext = '.mkv'
    recordingfile = home + desktop + 'video-' + time + ext
    
    # url from kwargs which is the dictionary passed to the function
    url = kwargs['url']

    rtmpcmd = "rtmpdump -q -i {0} | ffmpeg -hide_banner -stats -v panic -i - -c:v copy -c:a copy {1}".format(url, recordingfile)

    if 'duration' in kwargs:
        tflag = kwargs['tflag']
        duration = kwargs['duration']
        rtmpcmd = "rtmpdump -q -i {0} | ffmpeg -hide_banner -stats -v panic -i - -c:v copy -c:a copy {1} {2} {3}".format(url, tflag, duration, recordingfile)
    

    # split the ffmpeg command for subprocess
    rtmpsplit = shlex.split(rtmpcmd)

    print("running ffmpeg command:")
 
    # try ffmpeg function except keyboard interupt if user quits script with control c
    try:
        process = subprocess.run(rtmpsplit)
    except KeyboardInterrupt:
        print("recording stopped by user")
