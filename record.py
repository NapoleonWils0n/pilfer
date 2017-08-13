#!/usr/bin/env python3 

# record function
def ffmpeg(url, options=None, tflag=None, duration=None):
    recordingfile = 'recordingfile' 
    print("ffmpeg -hide_banner -stats -v panic", options, "-i", url, "-c:v copy -c:a copy", tflag, duration, recordingfile)
