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
        ud_split = urldata.split(r'|')
        ud_split_a = ud_split[0] # url before |
        ud_split_b = ud_split[1] # url after |

        print(master(ud_split_b))
        #return [ud_split_a, ud_split_b]
    elif rtmp.match(urldata):
        print("rtmp")
        urldata = {'url': urldata}
        return urldata
    elif localproxy.match(urldata):
        print("localproxy")
        urldata = {'url': urldata}
        return urldata
    else:
        print("full url")
        urldata = {'url': urldata}
        return urldata

# split string on = and store in dict
def split_equals(*args):
    return dict([v.split('=', 1) for v in args if '=' in v])
   
# regex dictionary
patterns = {
           'user-agent': 'u?User-a?Agent=[a-zA-Z0-9/.()\s,:;%+_-]+',
           'referer': 'r?Referer=[a-zA-Z0-9/.()\s,:;%+_-]+',
           'x-forward': 'X-Forwarded-For=[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',
           'cookie': '[cC]ookie=[a-zA-Z0-9/&%_*~;=_\s]+'
           }

urlparams = ''

def match_func(pattern, urlparams):
    def match_rule(urlparams):
        for match in re.finditer(pattern, urlparams):
            n = match.group()
            print(n)

    return match_rule

rules = [match_func(pattern, urlparams) for (pattern) in patterns.values()]

def master(urlparams):
    for match_func in rules:
        if match_func(urlparams):
            return match_func(urlparams)
