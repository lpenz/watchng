[![Build Status](https://travis-ci.org/lpenz/watchng.png?branch=master)](https://travis-ci.org/lpenz/watchng)

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


