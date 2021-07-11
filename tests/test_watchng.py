#!/usr/bin/env python3
#
# Copyright (C) 2012 Leandro Lisboa Penz <lpenz@lpenz.org>
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
"""Tests for watchng"""

import unittest

import watchng


class TestWatchng(unittest.TestCase):
    def test_watchng(self):
        start = watchng.time()
        maxrows, _ = watchng.consolesize()
        watchng.run1("sleep 2", maxrows=maxrows, shell=True)
        assert watchng.time() - start >= 2


if __name__ == "__main__":
    unittest.main()
