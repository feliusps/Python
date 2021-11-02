"""program a cash register for a warehouse.
 The system must be able to scan a product (the cashier can type in the product code), 
 and add it to the list of products purchased for that customer.
 It should also show the subtotal. The cashier can finish the purchase whenever
 he wishes and the system must apply the corresponding discounts to the products.
 Then, the cashier indicates how much the customer pays with and the system must 
 show the change to be returned to the customer. do the models and 
 tests of the functionalities. It is not necessary to make a graphical interface
 (or console), but the whole operation can be validated with the unit tests."""

import unittest
#test cases are represented by unittest.TestCase instances.
class RetailItem:
    def __init__(self, description, inventory, price):
        self.__description = description
        self.__inventory = inventory
        self.__price = price
    
    def set_description(self, description):
        self.__description = description
    
    def set_inventory(self, inventory):
        self.__inventory = inventory

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description
    
    def get_inventory(self):
        return self.__inventory
    
    def get_price(self):
        return self.__price
    
    def __str__(self):
        result = 'Description: ' + self.get_description() + '\n' + \
                 'Units in inventory: ' + str(self.get_inventory()) + \
                 '\nPrice: $' + str(self.get_price())
        return result

#=========================================================
#*******TESTING********
#=========================================================

class Test(unittest.TestCase):
    #@unittest.skip("Reazon for skipping")#Unconditionally skip the decorated test. reason should describe why the test is being skipped.
    
    
#********description method********
    #assertTrue compare test value with true
    #create a method to check if the parameter description in empty
    def is_empty(description):
        if(len(description) == 0):
           return True
        else:
           return False

    #assertTrue compare test value with true assert that two object are True
    def test_is_empty_empty_string_success(self):
        result = Test.is_empty("")
        self.assertTrue(result, True)

    #assertFalse compare test value with false
    def test_is_empty_with_string_success(self):
        result = Test.is_empty("description")
        self.assertFalse(result, False)


#********inventary method********

#assertTrue compare test value with true
    #create a method to check if the parameter description in empty
    def is_empty(inventory):
        if(len(inventory) == 0):
           return True
        else:
           return False

    #assertTrue compare test value with true assert that two object are True
    def test_is_empty_empty_string_success(self):
        result = Test.is_empty("")
        self.assertTrue(result, True)

    #assertFalse compare test value with false
    def test_is_empty_with_string_success(self):
        result = Test.is_empty("inventory")
        self.assertFalse(result, False)

#********price method********

#write  unittest to test the funcionality
    #assertEqual check for expected result
    def test_number_division_success(self):
        result = Test.price(19.99, (19.99 *.1))
        self.assertEqual(result, 1.9999) #1.9999 is the spected result
