import os 
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
from git import Repo
from requests.auth import HTTPBasicAuth

import argparse
import json
import os
import requests
import sys

def get_repos(username, password, team):
    bitbucket_api_root = 'https://api.bitbucket.org/1.0/users/'
    raw_request = requests.get(bitbucket_api_root + team, auth=HTTPBasicAuth(username, password))
    dict_request = json.loads(raw_request.content.decode('utf-8'))
    repos = dict_request['repositories']

    return repos

parser = argparse.ArgumentParser(description='clooney - clone all repos from a given BitBucket team/user')

parser.add_argument('-f',
                    '--full-path',
                    dest='full_path',
                    required=False,
                    help='Full path of directory which will hold the cloned repos')

parser.add_argument('-u',
                    '--username',
                    dest="username",
                    required=True,
                    help='Bitbucket username')

parser.add_argument('-p',
                    '--password',
                    dest="password",
                    required=False,
                    help='Bitbucket password')

parser.add_argument('-t',
                    '--team',
                    dest="team",
                    required=False,
                    help='The target team/user')

parser.set_defaults(full_path='')
parser.set_defaults(password='')
parser.set_defaults(team='')

args = parser.parse_args()

username = args.username
password = args.password
full_path = args.full_path
team = args.team