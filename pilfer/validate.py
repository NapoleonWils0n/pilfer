#!/usr/bin/env python3 

import sys, re, getopt, os.path, mimetypes

def usage():
    '''script usage
    
    display script usage when the -h or --help option is used
    '''
    usage = """
-h --help display help
-i 'video url' or text file
-t '00:00:00'

pilfer -i <video-url> -t <00:00:00>
    """
    print(usage)

def usageplay():
    '''script usage
    
    display script usage when the -h or --help option is used
    '''
    usageplay = """
-h --help display help
-i 'video url' or text file

pilfer-play -i <video-url>
    """
    print(usageplay)

def checkurl(url):
    ''' check first argument passed to script
    
    check if first argument passed to script, 
    is a text file and if so open it and read the contents,
    and set the variable url to equal the contents of the text file.
    if the first argument isnt a text file its on the command line
    
    then check if the string is a url
    '''
    if os.path.isfile(url):
        if mimetypes.guess_type(url)[0] == 'text/plain':
            with open(url, 'r') as file:
                url = file.read()
            file.close()          
            return url

    x = re.compile(r'^(http|https|rtmp|rtmpe)://.*$')
    if not x.match(url):
        usage()    # display script usage
        sys.exit() # exit
    return url
    
def durationValidated(duration):
    ''' validate user input for second argument

    user regular expressions to check duration matches 00:00:00 format
    '''
    y = re.compile('^[0-9]{2}:[0-9]{2}:[0-9]{2}$')
    if not y.match(duration):
        usage()    # display script usage
        sys.exit() # exit
    return duration
