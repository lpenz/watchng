#!/usr/bin/env python
'''Tests for watchng'''

import unittest

import watchng


class TestWatchng(unittest.TestCase):
    def test_watchng(self):
        start = watchng.uptime()
        maxrows, _ = watchng.consolesize()
        watchng.run1('sleep 2', maxrows=maxrows, shell=True)
        assert watchng.uptime() - start >= 2


if __name__ == '__main__':
    unittest.main()
