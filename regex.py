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
    rtmp = re.compile(r'^[rtmp|rtmpe]://')
    amp = re.compile(r'(?=[&][a-zA-Z_]+=+[-a-zA-Z0-9.]?)')
    if '|' in urldata:
        print("match |\n")
        ud = urldata.split(r'|')
        a = ud[0]
        b = ud[1]
        print("before slash:")
        print(a,"\n")
        print("after slash:")
        print(b)
        #udsplit = [v.split('=', 1) for v in ud if '=' in v]
        #urldata = dict(udsplit)
        print("full url:")
        return urldata
    elif rtmp.match(urldata):
        print("rtmp")
        return urldata
    elif localproxy.search(urldata):
        print("localproxy")
        return urldata
    else:
        return urldata

