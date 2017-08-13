#!/usr/bin/env python3 

# record function
def record(url, options=None, tflag="-t", duration=None):
    recordingfile = 'recordingfile' 
    print("ffmpeg -hide_banner -stats -v panic", options, "-i", url, "-c:v copy -c:a copy", tflag, duration, recordingfile)
