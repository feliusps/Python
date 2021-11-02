


import unittest

class testunittest(unittest.TestCase):

    def check_number_is_even(number):
        if (number <=0):
            return False
        elif (number % 2) == 0:
            return True
        else:
            return False


    #runtest debug test
    def test_number_even_successfuk(self):
        result = testunittest.check_number_is_even(4)
        self.assertEqual(result, True)

    #run test debug test
    def test_number_odd_successful(self):
        result = testunittest.check_number_is_even(3)
        self.assertEqual(result, False)

    #negative number
    def test_number_negative_fail(self):
        result = testunittest.check_number_is_even(-3)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()