import unittest
from kata import add

class TestAdd(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(add(''), 0)
        self.assertEqual(add('1'), 1)
        self.assertEqual(add('1,2'), 3)
        self.assertEqual(add('1\n,2,3'), 6)
        self.assertEqual(add('//;\n1;2'), 3)
        
        with self.assertRaises(Exception) as context:
            add('-1,2')

        self.assertTrue('Negatives not allowed: [-1]' in str(context.exception))

        with self.assertRaises(Exception) as context:
            add('-1,-2,2')

        self.assertTrue('Negatives not allowed: [-1, -2]' in str(context.exception))
