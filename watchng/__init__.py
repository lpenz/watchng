#!/usr/bin/python
""" A tool to synchronize the current directory remotly using FTP.

For usage, run ``watchng --help``.
"""

import sys
import os
import subprocess
import hashlib
import datetime
import uptime as upt
from time import sleep

PROGRAM_NAME = "watchng"
PROGRAM_VERSION = "1.3.0"

__version__ = PROGRAM_VERSION

# Useful functions: ##########################################################


def consolesize():
    fd = os.popen('stty size', 'r')
    for l in fd:
        rows, columns = l.split()
        return int(rows), int(columns)
    return None, None


def uptime():
    return upt.uptime()


# Core function: #############################################################


def run1(args, maxrows, shell=False):
    p = subprocess.Popen(
        args, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
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
