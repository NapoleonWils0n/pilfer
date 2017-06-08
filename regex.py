#!/usr/bin/env python3 

import re

#=================================================#
# split url
#=================================================#

def splitUrl(urldata):
    ''' split url
    
    split url on slash or ampersand
    '''
    slash = re.compile(r'^(http|https)://[a-zA-Z0-9:0-9./?=_,@&%-]+\.(m3u8|mkv|mp4|avi|flv)[|]+.*$')
    ampersand = re.compile(r'^(http|https)://[a-zA-Z0-9:0-9./?=_,@&%-]+(?=[&][a-zA-Z_]+=+[-a-zA-Z0-9.]?).*$')
    qmark = re.compile(r'^(http|https)://[a-zA-Z0-9:0-9./?=_,@&%-]+\.(m3u8|mkv|mp4|avi|flv)[?]+([a-zA-Z0-9?&=%*_-]*[^|])+.*$')
    if slash.match(urldata):
        print("match |")
        return urldata
    elif ampersand.match(urldata):
        print("match &")
        return urldata
    elif qmark.match(urldata):
        print("match ?")
        return urldata
    else:
        print("no match")
        return urldata

