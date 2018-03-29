[![Build Status](https://travis-ci.org/lpenz/watchng.png?branch=master)](https://travis-ci.org/lpenz/watchng)
[![codecov](https://codecov.io/gh/lpenz/watchng/branch/master/graph/badge.svg)](https://codecov.io/gh/lpenz/watchng)
[![PyPI version](https://badge.fury.io/py/watchng.svg)](https://badge.fury.io/py/watchng)


watchng
=======


# About

watchng is a program that runs the given command-line periodically, showing the
output only when it is different than the last, along with the time.


# Usage

~~~[.sh]
watchng --help
watchng [--period=<n>] [--shell] <command...>
~~~


## Options

**-h, --help** Help.

**-p, --period seconds** Set the interval between command executions

**-c, --shell** Run command through shell - as $SHELL -c <command...>

