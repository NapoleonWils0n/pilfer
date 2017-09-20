#!/usr/bin/env python3 

import shlex
import sys, os
import subprocess

def play(**kwargs):
    ''' play function

    mpv function
    '''
    if sys.platform.startswith('linux'):
        mpv = 'mpv'
    elif sys.platform.startswith('freebsd'):
        mpv = 'mpv'
    elif sys.platform.startswith('win32'):
        mpv = 'C:/pilfer/system/bin/mpv'
    elif sys.platform.startswith('darwin'):
        mpv = '/Applications/mpv.app/Contents/MacOS/mpv'

    # get the values from the dictionary passed to the function
    values = list(kwargs.values())
    # url from kwargs which is the dictionary passed to the function
    url = kwargs['url']

    mpvcmd = "{0} {1}".format(mpv, url)

    if any(word in kwargs for word in ('user-agent', 'referer', 'cookie')):                 
        # dict minus first time which is the url
        options = values[1:]
        remove_bracket = str(options)[1:-1]
        options_join = ''.join(remove_bracket).replace('"', '')
        mpvcmd = "{0} {2} {1}".format(mpv, url, options_join)

    # split the mpv command for subprocess
    mpvsplit = shlex.split(mpvcmd)

    print("running mpv command:")
 
    # try mpv function except keyboard interupt if user quits script with control c
    try:
        process = subprocess.run(mpvsplit)
    except KeyboardInterrupt:
        print("recording stopped by user")
    except IOError:
        print("input outpur error, is mpv installed")


def rtmpplay(**kwargs):
    ''' rtmp play function

    mpv function
    '''
    if sys.platform.startswith('linux'):
        rtmpdump = 'rtmpdump'
        mpv = 'mpv'
    elif sys.platform.startswith('freebsd'):
        rtmpdump = 'rtmpdump'
        mpv = 'mpv'
    elif sys.platform.startswith('win32'):
        rtmpdump = 'C:/pilfer/system/bin/rtmpdump'
        mpv = 'C:/pilfer/system/bin/mpv'
    elif sys.platform.startswith('darwin'):
        rtmpdump = '/usr/local/bin/rtmpdump'
        mpv = '/Applications/mpv.app/Contents/MacOS/mpv'

    # get the values from the dictionary passed to the function
    values = list(kwargs.values())
    # url from kwargs which is the dictionary passed to the function
    url = kwargs['url']

    # rtmpdump mpv command
    rtmpcmd = "{0} -q -i '{1}' | {2} -".format(rtmpdump, url, mpv)
    
    print("running mpv command:")
 
    # try mpv function except keyboard interupt if user quits script with control c
    try:
        process = subprocess.run(rtmpcmd, shell=True)
    except KeyboardInterrupt:
        print("recording stopped by user")
    except IOError:
        print("input outpur error, is mpv installed")
