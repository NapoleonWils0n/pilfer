#!/usr/bin/env python3 

# record function
def record(link, *args):
    arg2 = args[0:]
    strtuple = ' '.join(arg2)
    print(strtuple)
            
    print("ffmpeg -hide_banner -stats -v panic", strtuple, "-i", link, "-c:v copy -c:a copy $tflag $duration $recordingfile")
