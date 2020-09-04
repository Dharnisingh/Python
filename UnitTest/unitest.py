# Program to demonstrate the Unittest module

import unittest

# Create a class which will be inherited from uniteest.TestCase and hold all the test cases
class testMyModules(unittest.TestCase):
    def test_UpperStr(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_IsUpper(self):
        self.assertTrue('FOO'.isupper())
    
    def test_Sum(self):
        # This testcase should fail
        self.assertEqual(sum([4,5]), 9)


if __name__ == '__main__':
    unittest.main()
