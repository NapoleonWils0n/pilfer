#!/usr/bin/env python3

from pilfer import validate, regex, play
import sys, re, getopt, os.path, mimetypes

# argv
argv = sys.argv[1:]

# shortcuts for imported functions
usage = validate.usageplay
checkurl = validate.checkurl
splitUrl = regex.splitUrl
splitEquals = regex.splitEquals

# url and duration
result = []

#=================================================#
# main function
#=================================================#

def main(argv):
    ''' main function
    
    check number of arguments passed to script
    '''
    if len(argv) == 0: # no arguments passed to script
        print("No arguments passed to script")
        usage()    # display script usage
        sys.exit() # exit
    elif len(argv) > 2: # too many arguments passed to script
        print("Too many arguments passed to script")
        usage()    # display script usage
        sys.exit() # exit

    try:
        opts, args = getopt.getopt(argv, "hi:", ["help", "url"])
    except getopt.GetoptError as err: 
        print(err)  # will print something like "option -x not recognized"
        usage()     # display script usage
        sys.exit(2) # exit

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            # -h or --help = display help
            usage()
            sys.exit()
        elif opt == ("-i") and len(argv) == 2:
            # -i and url or text file
            result.append(checkurl(argv[1]))
            return result
        else:
            assert False, "unhandled option"

#=================================================#
# slice off script name from arguments
#=================================================#

if __name__ == "__main__":
    main(sys.argv[1:])

    # the validated url
    url = result[0]

    # the url stored in a dictionary
    theUrl = splitUrl(url)
    
    # url dictionary keys lowercased for searching
    urlDict = {k.lower(): v for k, v in theUrl.items()}

    # play dictionary to hold url and ffmpeg options
    playDict = {}

    if 'url' in urlDict:
        ul = urlDict['url']
        url = '{0}'.format(ul)
        playDict['url'] = url

    if 'user-agent' in urlDict:
        ua = urlDict['user-agent']
        useragent = "--user-agent='{0}'".format(ua)
        playDict['user-agent'] = useragent

    if 'referer' in urlDict:
        rf = urlDict['referer']
        referer = "--referrer='{0}'".format(rf)
        playDict['referer'] = referer

    if 'cookie' in urlDict:
        cd = re.search('(http|https)://[a-zA-Z0-9.-]*[^/]', url) # cookie domain name
        cookiedomain = cd.group()
        cookieurl = urlDict['cookie']
        cookie = "--http-header-fields='cookie: {0}; path=/; {1};'".format(cookieurl, cookiedomain)
        playDict['cookie'] = cookie

    nltid = re.findall('nltid=[a-zA-Z0-9&%_*=]*', url) # nltid cookie in url

    if nltid:
        cd = re.search('(http|https)://[a-zA-Z0-9.-]*[^/]', url) # cookie domain name
        cookiedomain = cd.group()
        cookieurl = nltid[0]
        cookie = "--http-header-fields='cookie: {0}; path=/; {1};'".format(cookieurl, cookiedomain)
        playDict['nltid'] = cookie

    # http and rtmp regexes
    http = re.compile(r'^(http|https)://')
    rtmp = re.compile(r'^(rtmp|rtmpe)://')

    # check if http or rtmp link
    if http.match(url):
        play = play.play(**playDict)
    elif rtmp.match(url):
        rtmpplay = play.rtmpplay(**playDict)
