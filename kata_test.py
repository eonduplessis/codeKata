import unittest
from kata import add

class TestAdd(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(add(""), 0)
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("1,2"), 3)