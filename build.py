#!/usr/bin/python

from subprocess import call
from github import Github
import re
from sys import argv

if (len(argv) == 2):
    call(["mkdir", "docs"])

    serviceMatch = re.compile("service-((?!skeleton)\w+)")
    for repo in Github(argv[1]).get_organization('0xhexspeak').get_repos() :
        serviceNameMatch = serviceMatch.match(repo.name)
        if serviceNameMatch :
            # svn export https://github.com/0xHEXSPEAK/service-oauth/trunk/api/web/doc ./oauth/
            call(["svn", "export", repo.svn_url + "/trunk/api/web/doc", "docs/" + serviceNameMatch.group(1), "--force"])
            print serviceNameMatch.group(1)

    call(["surge", "docs/", "0xhexspeak.surge.sh"])
else:
    print "Specify your github token"
