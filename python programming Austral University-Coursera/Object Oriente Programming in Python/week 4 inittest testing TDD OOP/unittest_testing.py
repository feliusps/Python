
"""unittest basic definition way of testing a small unit of code
the first level of software testing where the smallest testable 
parts of a software are tested. This is used to validate that 
each unit of the software performs as designed."""

import unittest
#test cases are represented by unittest.TestCase instances.
class Test(unittest.TestCase):
    #@unittest.skip("Reazon for skipping")#Unconditionally skip the decorated test. reason should describe why the test is being skipped.
    
    #create a method division
    def division(numberOne, numberTwo):
        result = numberOne / numberTwo
        return result

    #write  unittest to test the funcionality
    #assertEqual check for expected result
    def test_number_division_success(self):
        result = Test.division(6, 2)
        self.assertEqual(result, 3) #three 3 is the spected result

    #asserNotEqual check for the inequality of two values.
    def test_number_division_noequal(self):
        result = Test.division(6, 2)
        self.assertNotEqual(result, 4) #use 3 and 4

    #assertTrue compare test value with true
    #create a method to check if the parameter word in empty
    def is_empty(word):
        if(len(word) == 0):
           return True
        else:
           return False

    #assertTrue compare test value with true assert that two object are True
    def test_is_empty_empty_string_success(self):
        result = Test.is_empty("")
        self.assertTrue(result, True)

    #assertFalse compare test value with false
    def test_is_empty_with_string_success(self):
        result = Test.is_empty("Hello")
        self.assertFalse(result, False)

    #exception Test
    """assertRaises() – It allows an exception to be encapsulated, meaning that 
    the test can throw an exception without exiting the execution, 
    as is normally the case for unhandled exceptions"""
    # create a method division
    def division(numberOne, numberTwo):
        result = numberOne / numberTwo
        return result

    def testRaises(self): 
         self.assertRaises(ZeroDivisionError, Test.division, 1, 0)      
     
if __name__ == '__main__':
        unittest.main()