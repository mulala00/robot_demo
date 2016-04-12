#! /usr/bin/env python

"""Runner Script for Robot Framework SeleniumLibrary Demo

Tests are run by giving a path to the tests to be executed as an argument to
this script. Possible Robot Framework options are given before the path.

Examples:
  rundemo.py login_tests                        # Run all tests in a directory
  rundemo.py login_tests/valid_login.text       # Run tests in a specific file
  rundemo.py --variable BROWSER:IE login_tests  # Override variable
  rundemo.py -v BROWSER:IE -v DELAY:0.25 login_tests

By default tests are executed with Firefox browser, but this can be changed
by overriding the `BROWSER` variable as illustrated above. Similarly it is
possible to slow down the test execution by overriding the `DELAY` variable
with a non-zero value.

When tests are run, the demo application is started and stopped automatically. 
It is also possible to start and stop the application separately
by using `demoapp` options. This allows running tests with the
normal `pybot` start-up script, as well as investigating the demo application.

Running the demo requires that Robot Framework, Selenium2Library, Python, and
Java to be installed.
"""

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
