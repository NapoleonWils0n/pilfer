#!/usr/bin/env python3 

import re

#=================================================#
# split url
#=================================================#

def splitUrl(url_to_split):
    ''' split url
    
    split url on slash or ampersand
    '''
    slash = re.compile(r'^(http|https)://[a-zA-Z0-9:0-9./?=_,@&%-]+\.(m3u8|mkv|mp4|avi|flv)[|]+.*$')
    ampersand = re.compile(r'^(http|https)://[a-zA-Z0-9:0-9./?=_,@&%-]+(?=[&][a-zA-Z_]+=+[-a-zA-Z0-9.]?).*$')
    qmark = re.compile(r'^(http|https)://[a-zA-Z0-9:0-9./?=_,@&%-]+\.(m3u8|mkv|mp4|avi|flv)[?]+([a-zA-Z0-9?&=%*_-]*[^|])+.*$')
    if slash.match(url_to_split):
        print("match |")
    elif ampersand.match(url_to_split):
        print("match &")
        return url_to_split
    elif qmark.match(url_to_split):
        print("match ?")
    else:
        print("no match")
