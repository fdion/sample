# -*- coding: utf-8 -*-
import unittest

import toxsample

class TestToxSample(unittest.TestCase):
    
    def test_is_shiningpanda_amazing(self):
        self.assertTrue(toxsample.is_shiningpanda_amazing())

    def test_fail_on_3(self):
        print("Not gonna happen")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
