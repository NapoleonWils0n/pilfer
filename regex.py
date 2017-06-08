#!/usr/bin/env python3 

import re

#=================================================#
# split url
#=================================================#

def splitUrl(urldata):
    ''' split url
    
    split url on slash or ampersand
    '''
    slash = re.compile(r'|')
    amp = re.compile(r'(?=[&][a-zA-Z_]+=+[-a-zA-Z0-9.]?)')
    if '|' in urldata:
        print("match |")
        return urldata
    elif amp.match(urldata):
        print("match &")
        return urldata
    else:
        print("no match")
        return urldata

