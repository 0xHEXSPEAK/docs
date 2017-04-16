# SurgeDoc

![surgedoc](http://githubimg.surge.sh/surgedoc.png "SurgeDoc Logo")

**What it does?**

This script automates the proccess of fetching and publishing docs from github organization repositories using [Surge](https://surge.sh).

**How to run?**

1) You should have installed `surge`, `svn` and `pip` on your computer.
2) Install script dependencies using pip by executing the following command:

```pip install -r requirements.txt```

3) Change default sync domain in CNAME to yours 
4) Run this commands in your shell to start fetch and publish proccess:

```chmod a+x surgedoc.py ```

```./surgedoc.py [--docs <custom_path_to_docs>] [--regex <regular_expression>] <organization_name> <github_token>```