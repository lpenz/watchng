#!/usr/bin/python
""" A tool to synchronize the current directory remotly using FTP.

For usage, run ``watchng --help``.
"""

import sys
import os
import subprocess
import hashlib
import datetime
from time import sleep
from uptime import uptime

PROGRAM_NAME = "watchng"
PROGRAM_VERSION = "1.2.0"

__version__ = PROGRAM_VERSION

# Useful functions: ##########################################################


def consolesize():
    rows, columns = os.popen('stty size', 'r').read().split()  # rows, columns
    return int(rows), int(columns)


# Core function: #############################################################


def run1(args, maxrows, shell=False):
    p = subprocess.Popen(
        args,
        shell=shell,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    rv = []
    rows = 0
    m = hashlib.md5()
    for l in p.stdout:
        rv.append(l)
        m.update(l)
        rows += 1
        if rows > maxrows - 3:
            p.kill()
            break
    p.wait()
    return rv, m.hexdigest()


def runall(args, period=1, shell=False):
    maxrows, maxcolumns = consolesize()
    outlast = None
    while True:
        start = uptime()
        output, outhash = run1(args, maxrows, shell=shell)
        if outlast and outlast == outhash:
            continue
        if outlast is not None:
            sys.stdout.write('\n')
        sys.stdout.write('$ %s # every %d seconds, last at %s\n' %
                         (' '.join(args), period,
                          str(datetime.datetime.now())))
        for l in output:
            sys.stdout.write(l[:maxcolumns])
        outlast = outhash
        sleep(max(0, period - (uptime() - start)))
