[![CI](https://github.com/lpenz/watchng/actions/workflows/ci.yml/badge.svg)](https://github.com/lpenz/watchng/actions/workflows/ci.yml)
[![coveralls](https://coveralls.io/repos/github/lpenz/watchng/badge.svg?branch=main)](https://coveralls.io/github/lpenz/watchng?branch=main)
[![packagecloud](https://img.shields.io/badge/deb-packagecloud.io-844fec.svg)](https://packagecloud.io/app/lpenz/debian/search?q=watchng)


# watchng

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

