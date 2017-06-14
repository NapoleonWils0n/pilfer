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
    rtmp = re.compile(r'^(rtmp|rtmpe)://')
    amp = re.compile(r'(?=[&][a-zA-Z_]+=+[-a-zA-Z0-9.]?)')
    if '|' in urldata:
        print("match |")
        ud = urldata.split(r'|')
        a = ud[0] # url before |
        b = ud[1] # url after |
        print(userAgent(b))
        print(cookie(b))
        return a
    elif rtmp.match(urldata):
        print("rtmp")
        return urldata
    elif localproxy.match(urldata):
        print("localproxy")
        return urldata
    else:
        print("full url")
        return urldata

def splitEquals(eq):
    return dict([v.split('=', 1) for v in eq if '=' in v])
    
def match_func(pattern, urlparams):
    def match_rule(urlparams):
        return re.findall(pattern, urlparams)
    return match_rule
    
def userAgent(params):
    return re.findall(r'u?User-a?Agent=[a-zA-Z0-9/.()\s,:;%+_-]+', params)
   
def cookie(params):
    return re.findall(r'[cC]ookie=[a-zA-Z0-9/&%_*~;=_\s]+', params) 
           
#    splitEquals(f)

#    if cookie.findall(params):
#        f = cookie.findall(params)
#        fsplit = [v.split('=', 1) for v in f if '=' in v]
#        print(fsplit)
 
#   if useragent.findall(params):
#        c = useragent.findall(params)
#        csplit = [v.split('=', 1) for v in c if '=' in v]
#        d = dict(csplit)
#        for k, v in d.items():
#            print(k, v)
        #return d['User-Agent']
