#!/usr/bin/env python3
import argparse
from json import dumps
from os import name, system
from sys import argv

from vang.tfs.api import call


def create_repo(repo):
    organisation, project, name = repo.split('/')
    return call(
        f'/{organisation}/{project}/_apis/git/repositories?api-version=3.2',
        request_data=dumps({
            'name': name
        }),
        method='POST',
    )


def main(repo):
    response = create_repo(repo)
    commands = '    git remote add origin {}\n' \
               '    git push -u origin develop'.format(response['remoteUrl'])
    print('If you already have code ready to be pushed to this repository '
          'then run this in your terminal.')
    print(commands)
    if name == 'posix':
        system('echo "{}\c" | pbcopy'.format(commands))
        print('(The commands are copied to the clipboard)')


def parse_args(args):
    parser = argparse.ArgumentParser(description='Create TFS repository')
    parser.add_argument(
        'repo',
        help='The TFS repository to create, e.g. organisation/project/repo1')
    return parser.parse_args(args)


if __name__ == '__main__':
    args = parse_args(argv[1:])
    main(args.repo)