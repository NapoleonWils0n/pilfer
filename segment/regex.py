#!/usr/bin/env python3 

import re
from urllib.parse import unquote

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
    
    split url on slash
    '''
    if '|' in urldata:
        ud_split = urldata.split(r'|')
        ud_split_a = ud_split[0] # url before |
        ud_split_b = ud_split[1] # url after |
        ud_decode = unquote(unquote(ud_split_b))
        data = splitEquals(master(ud_decode)) # create the url dictionary
        data['url'] = ud_split_a # add the url to the dictionary
        return data
    else:
        data = {'url': urldata}
        return data


# regex patterns
patterns = {
           'user-agent': '[uU]ser-[aA]gent=[a-zA-Z0-9/.()\s,:;%+_-]+',
           'referer': '[rR]eferer=[a-zA-Z0-9/.()\s,:;%+_-]+',
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
