#!/usr/bin/env python3

import argparse
from sys import argv

from vang.tfs.api import call


def get_projects(organisations, project_specs=False, names=False):
    projects = [(o, p) for o in organisations
                # for p in call(f'/{o}/_apis/projects?api-version=3.2')['value']]
                for p in call(f'/{o}/_apis/projects')['value']]

    if names:
        return [project[1]['name'] for project in projects]
    if project_specs:
        return [f'{project[0]}/{project[1]["name"]}' for project in projects]

    return projects


def parse_args(args):
    parser = argparse.ArgumentParser(description='Get TFS projects')
    parser.add_argument(
        'organisations', nargs='+', help='TFS organisations, e.g organisation')
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        '-n', '--names', action='store_true', help='Get only project names')
    parser.add_argument(
        '-p',
        '--project_specs',
        action='store_true',
        help='Get only organisation/project')

    return parser.parse_args(args)


if __name__ == '__main__':
    pargs = parse_args(argv[1:])

    for a_project in get_projects(
            pargs.organisations,
            pargs.project_specs,
            pargs.names,
    ):
        print(a_project)
