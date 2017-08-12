#!/usr/bin/env python3 

# record function
def record(link, options, *args):
            
    print("ffmpeg -hide_banner -stats -v panic", options, "-i", link, "-c:v copy -c:a copy $tflag $duration $recordingfile")
