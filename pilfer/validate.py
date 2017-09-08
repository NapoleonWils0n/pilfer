#!/usr/bin/env python3 

import sys, re, getopt, os.path, mimetypes

#=================================================#
# sys       = system access to open files
# re        = regular expressions
# getopt    = check script arguments and options
# os.path   = check if first argument is a file
# mimetypes = check if file is a text file
#=================================================#


#=================================================#
# script usage function
#=================================================#

def usage():
    '''script usage
    
    display script usage when the -h or --help option is used
    '''
    usage = """
-h --help display help
-i 'video url'
-t '00:00:00'

rip-record -i <video-url> -t <00:00:00>
    """
    print(usage)


#=================================================#
# checkurl function - check if first arg is text file
#=================================================#

# pass argv[1] which is the first argument with the url -
# to the checkurl function
# use os.path.isfile to check if the the first arg -
# is a file, then use mimetypes to check if its a text file
# if it is a text file, read the contents -
# and set the variable url to equal the contents of the text file
# if its not a text file - url variable is 
# the function just prints the url at the moment
# should return the url


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

#=================================================#
# validation functions
#=================================================#

# functions to validate the url which comes after -i
# and the duration which comes after -t

# the url should start with http|https|rtmp|rtmpe://
# the duration should match 00:00:00 format
# 0-9 followed by : 0-9 followed by : 0-9 followed by :

# these are the bash regular expressions which should work with python
# the function should validate the url and duration with regulat expressions
# and if the user input doesnt match the regexs display script usage and exit

def durationValidated(duration):
    ''' validate user input for second argument

    user regular expressions to check duration matches 00:00:00 format
    '''
    y = re.compile('^[0-9]{2}:[0-9]{2}:[0-9]{2}$')
    if not y.match(duration):
        usage()    # display script usage
        sys.exit() # exit
    return duration

#=================================================#
# check number of arguments passed to script
#=================================================#

def argLength(arglen):
    ''' check number of arguments

    check if 0 or more than 4 arguments passed to script
    '''
    if len(arglen) == 0:  # no arguments passed to script
        print("No arguments passed to script")
        usage()    # display script usage
        sys.exit() # exit
    elif len(arglen) > 4: # too many arguments passed to script
        print("Too many arguments passed to script")
        usage()    # display script usage
        sys.exit() # exit
