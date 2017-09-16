#!/usr/bin/env python3 

import shlex
import sys, os
import subprocess
from datetime import datetime 

def ffmpeg(**kwargs):
    ''' ffmpeg function

    ffmpeg recording function
    '''
    home = os.path.expanduser('~')
    desktop = 'Desktop'
    time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ext = 'mkv'
    recordingfile = os.path.join(home, desktop, 'video-{}.{}'.format(time, ext))
    
    if sys.platform.startswith('linux'):
        ffmpeg = 'ffmpeg'
        rtmpdump = 'rtmpdump'
    elif sys.platform.startswith('freebsd'):
        ffmpeg = 'ffmpeg'
        rtmpdump = 'rtmpdump'
    elif sys.platform.startswith('win32'):
        home = os.path.expanduser('~').replace('\\', '/')
        desktop = '//Desktop//'
        time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        ext = '.mkv'
        recordingfile = home + desktop + 'video-' + time + ext
    elif sys.platform.startswith('darwin'):
        bin = 'bin'
        ffmpeg = os.path.join(home, bin, 'ffmpeg')

    # get the values from the dictionary passed to the function
    values = list(kwargs.values())
    # url from kwargs which is the dictionary passed to the function
    url = kwargs['url']

    ffcmd = "{0} -hide_banner -stats -v panic -i {1} -c:v copy -c:a copy {2}".format(ffmpeg, url, recordingfile)
    #ffcmd = "ffmpeg -hide_banner -stats -v panic -i {0} -c:v copy -c:a copy {1}".format(url, recordingfile)

    if any(word in kwargs for word in ('user-agent', 'referer', 'cookie')):                 
        # dict minus first time which is the url
        options = values[1:]
        remove_bracket = str(options)[1:-1]
        options_join = ''.join(remove_bracket).replace('"', '')
        #ffcmd = "ffmpeg -hide_banner -stats -v panic {1} -i {0} -c:v copy -c:a copy {2}".format(url, options_join, recordingfile)
        ffcmd = "{0} -hide_banner -stats -v panic {2} -i {1} -c:v copy -c:a copy {3}".format(ffmpeg, url, options_join, recordingfile)

    if 'duration' in kwargs:
        tflag = kwargs['tflag']
        duration = kwargs['duration']
        # dict minus first time which is the url, and minus the last 2 items tflag and duration
        options = values[1:-2]
        remove_bracket = str(options)[1:-1]
        options_join = ''.join(remove_bracket).replace('"', '')
        #ffcmd = "ffmpeg -hide_banner -stats -v panic {1} -i {0} -c:v copy -c:a copy {2} {3} {4}".format(url, options_join, tflag, duration, recordingfile)
        ffcmd = "{0} -hide_banner -stats -v panic {2} -i {1} -c:v copy -c:a copy {3} {4} {5}".format(ffmpeg, url, options_join, tflag, duration, recordingfile)


    # split the ffmpeg command for subprocess
    ffsplit = shlex.split(ffcmd)

    print("running ffmpeg command:")
 
    # try ffmpeg function except keyboard interupt if user quits script with control c
    try:
        process = subprocess.run(ffsplit)
    except KeyboardInterrupt:
        print("recording stopped by user")
    except IOError:
        print("input outpur error, is ffmpeg installed")


def rtmp(**kwargs):
    ''' rtmpdump function

    rtmpdump recording function
    '''
    home = os.path.expanduser('~')
    desktop = 'Desktop'
    time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ext = 'mkv'
    recordingfile = os.path.join(home, desktop, 'video-{}.{}'.format(time, ext))
    
    if sys.platform.startswith('linux'):
        ffmpeg = 'ffmpeg'
        rtmpdump = 'rtmpdump'
    elif sys.platform.startswith('freebsd'):
        ffmpeg = 'ffmpeg'
        rtmpdump = 'rtmpdump'
    elif sys.platform.startswith('win32'):
        home = os.path.expanduser('~').replace('\\', '/')
        desktop = '//Desktop//'
        time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        ext = '.mkv'
        recordingfile = home + desktop + 'video-' + time + ext
    elif sys.platform.startswith('darwin'):
        bin = 'bin'
        ffmpeg = os.path.join(home, bin, 'ffmpeg')
        rtmpdump = '/usr/local/bin/rtmpdump'


    # url from kwargs which is the dictionary passed to the function
    url = kwargs['url']

    rtmpcmd = "{0} -i '{1}' -o {2}".format(rtmpdump, url, recordingfile)

    if 'duration' in kwargs:
        tflag = kwargs['tflag']
        duration = kwargs['duration']
        rtmpcmd = "{0} -q -i '{1}' | {2} -hide_banner -stats -v panic -i - -c:v copy -c:a copy {3} {4} {5}".format(rtmpdump, ffmpeg, url, tflag, duration, recordingfile)

    print("running rtmp command:")
 
    # try ffmpeg function except keyboard interupt if user quits script with control c
    try:
        process = subprocess.run(rtmpcmd, shell=True)
    except KeyboardInterrupt:
        print("recording stopped by user")
    except IOError:
        print("input outpur error, is rtmpdump or ffmpeg installed")
