#!/usr/bin/env python3 

import re

#=================================================#
# split url
#=================================================#

# master 
result = []
urlparams = ''

# split string on = and store in dict
def splitEquals(tosplit):
    ''' split equals

    split url on equals
    '''
    data = dict([v.split('=', 1) for v in tosplit if '=' in v])
    return data

# split url on |
def splitUrl(urldata):
    ''' split url
    
    split url on slash or ampersand
    '''
    localproxy = re.compile(r'^http://127.0.0.1[:0-9]?')
    rtmp = re.compile(r'^(rtmp|rtmpe)://')
    #amp = re.compile(r'(?=[&][a-zA-Z_]+=+[-a-zA-Z0-9.]?)')
    if '|' in urldata:
        ud_split = urldata.split(r'|')
        ud_split_a = ud_split[0] # url before |
        ud_split_b = ud_split[1] # url after |
        data = splitEquals(master(ud_split_b))
        data['url'] = ud_split_a
        return data
    elif rtmp.match(urldata):
        data = {'url': urldata}
        return data
  #  elif localproxy.match(urldata):
  #      print("localproxy")
  #      data = {'url': urldata}
  #      return data
    else:
        data = {'url': urldata}
        return data


# regex patterns
patterns = {
           'user-agent': '[uU]ser-[aA]gent=[a-zA-Z0-9/.()\s,:;%+_-]+',
           'referer': '[rR]eferer=[a-zA-Z0-9/.()\s,:;%+_-]+',
           'x-forward': 'X-Forwarded-For=[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',
           'cookie': '[cC]ookie=[a-zA-Z0-9/&%_*~;=_\s]+'
           }

# master function calls match_func
def master(urlparams):
    ''' master function
    
    master function to split url 
    '''
    for match_func in rules:
        if match_func(urlparams):
            result.append(match_func(urlparams))
    return result

# match regular expressions
def match_func(pattern, urlparams):
    ''' match function

    match function to match regular expressions
    '''
    def match_rule(urlparams):
        itererator = re.finditer(pattern, urlparams)
        for match in itererator:
            return match.group()
    return match_rule

# rules must go after match_func
rules = [match_func(pattern, urlparams) for (pattern) in patterns.values()]
