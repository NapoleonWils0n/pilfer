#!/usr/bin/env python3 

import re

#=================================================#
# split url
#=================================================#

def splitUrl(urldata):
    ''' split url
    
    split url on slash or ampersand
    '''
    localproxy = re.compile(r'^http://127.0.0.1[:0-9]?')
    amp = re.compile(r'(?=[&][a-zA-Z_]+=+[-a-zA-Z0-9.]?)')
    if '|' in urldata:
        print("match |")
        return urldata
    elif localproxy.search(urldata):
        print("localproxy")
        return urldata
    elif amp.search(urldata):
        print("match &")
        return urldata
    else:
        return urldata

