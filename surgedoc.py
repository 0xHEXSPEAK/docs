#!/usr/bin/python

from subprocess import call
from github import Github
import re
import argparse

# CLI argumens configuration
parser = argparse.ArgumentParser()
parser.add_argument("organization", help="Github organization name")
parser.add_argument("token", help="Your github token")
parser.add_argument("--docs", help="Path to docs in organization repositories")
parser.add_argument("--regex", help="Regular expression to choose only specific repositories")
args = parser.parse_args()

docsPath = "/trunk/api/web/doc"
syncPath = "docs/"
regEx = "service-((?!skeleton)\w+)"

# Check for optional parameters
if args.docs :
    docsPath = args.docs
if args.regex :
    regEx = args.regex

# Build docs folder structure
serviceMatch = re.compile(regEx)
for repo in Github(args.token).get_organization(args.organization).get_repos() :
    serviceNameMatch = serviceMatch.match(repo.name)
    if serviceNameMatch :
        # svn export https://github.com/0xHEXSPEAK/service-oauth/trunk/api/web/doc ./oauth/
        call(["svn", "export", repo.svn_url + docsPath, syncPath + serviceNameMatch.group(1), "--force"])
        print serviceNameMatch.group(1)

# Sync domain configuration
call(["cp", "-fv", "CNAME", syncPath])

# Upload and remove all files locally
call(["surge", syncPath])
call(["rm", "-R", syncPath])
