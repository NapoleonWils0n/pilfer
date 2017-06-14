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
        print(len(b))
        print(master(b))
#        print(userAgent(b))
#        print(cookie(b))
        return (a, b)
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
    
urlparams = ''

def match_func(pattern, urlparams):
    def match_rule(urlparams):
        return re.findall(pattern, urlparams)
#        return splitEquals(re.findall(pattern, urlparams))
    return match_rule
    
rules = []
with open ('regex.txt', encoding='utf-8') as pattern_file:
    for line in pattern_file:
        pattern = line.split()
        rules.append(match_func(pattern))

#patterns = \
#    (
#        ('u?User-a?Agent=[a-zA-Z0-9/.()\s,:;%+_-]+'),
#        ('[cC]ookie=[a-zA-Z0-9/&%_*~;=_\s]+')
#    )
#
#rules = [match_func(pattern, urlparams) for (pattern) in patterns]

def master(urlparams):
    for match_func in rules:
        if match_func(urlparams):
            return match_func(urlparams)
