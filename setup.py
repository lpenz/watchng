#!/usr/bin/env python

from setuptools import setup
import re


def version_get():
    with open('watchng') as fd:
        for line in fd:
            m = re.match('^PROGRAM_VERSION = "(?P<version>[0-9.]+)"',
                         line)
            if m:
                return m.group('version')


setup(name="watchng",
      version=version_get(),
      description="Run a command periodically, "
      "showing output only when it changes",
      author="Leandro Lisboa Penz",
      author_email="lpenz@lpenz.org",
      url="http://github.com/lpenz/watchng",
      data_files=[('man/man1', ['watchng.1'])],
      scripts=["watchng"],
      long_description="""\
watchng is a program that runs the given command-line periodically, showing
the output only when it is different than the last, along with the time.
""",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'License :: OSI Approved :: '
          'GNU General Public License v2 or later (GPLv2+)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          ],
      license="GPL2")
