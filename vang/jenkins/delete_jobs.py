#!/usr/bin/env python3

import argparse
from sys import argv

from vang.jenkins.api import call


def delete_jobs(names):
    return [(job_name, call(
        f'/job/{job_name}/doDelete',
        method='POST',
        only_response_code=True,
    )) for job_name in names]


def parse_args(args):
    parser = argparse.ArgumentParser(description='Delete Jenkins jobs')
    parser.add_argument(
        'job_names',
        nargs='+',
        help='Jenkins job names',
    )
    return parser.parse_args(args)


if __name__ == '__main__':
    pargs = parse_args(argv[1:])
    for a_job_name, a_response_code in delete_jobs(pargs.job_names):
        print(a_job_name, a_response_code)
