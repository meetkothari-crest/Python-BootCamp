# 10. Write a Python unit test program to check if a function correctly parses and validates input data.

import unittest

def validate(input_data):
    return input_data.isnumeric()


class Test(unittest.TestCase):
    def test_valid(self):
        data = "123"
        res = validate(data)
        self.assertEqual(res, True)

    def test_invalid(self):
        data = 'abcd'
        res = validate(data)
        self.assertEqual(res,False)

if __name__ == '__main__':
    unittest.main()

