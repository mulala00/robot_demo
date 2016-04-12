#! /usr/bin/env python

"""
This the startup script for the demo

You can just using:
python rundemo.py for this case
"""

# TODO: Write The guide here

import os
import sys
from subprocess import call


ROOT = os.path.dirname(os.path.abspath(__file__))
LIB_PATH = os.path.join(ROOT, 'libraries')


def gen_common_args():
    return "-Acommon_arguments.txt"


def gen_robot_args(case):
    arg = list()
    arg.append(gen_common_args())
    if case is None:
        arg.append(r"testcases")
    else:
        arg.append(case)
    return arg


def run_tests(case=None):
    cmd = ["robot"]
    cmd.extend(gen_robot_args(case))
    call(cmd, shell=(os.sep == '\\'))

if __name__ == '__main__':
    # TODO: Need to start the RobotRemoteServer before the Remote Demo, using python library/remote_server_demo.py
    if len(sys.argv) > 1:
        run_tests(sys.argv[1])
    else:
        run_tests()
