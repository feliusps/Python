
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
class CashRegister:
# initialize an empty list to hold purchased items
    def __init__(self):
        self.__items = []
# method that clears the contents of the cash register
    def clear(self):
        self.__items = []
# method that simulates adding an item to the cash register.
# receives a RetailItem object as an argument.
    def purchase_item(self, retail_item):
        self.__items.append(retail_item)
        print("The item was added to the cash register.")
# method returning the total cost of items at the cash register.
    def get_total(self):
        total = 0.0
        for item in self.__items:
            total = total + item.get_price()
        return total
# method that prints a list of items at the cash register.
    def show_items(self):
        print("The items in the cash register are:")
        print()
        for item in self.__items:
            print(item)
            print()

#=============================================================== 
#******* TESTING*******
#===============================================================

class Test(unittest.TestCase):
    #@unittest.skip("Reazon for skipping")#Unconditionally skip the decorated test. reason should describe why the test is being skipped.
    
    #assertTrue compare test value with true
    #create a method to check if the parameter retail_item in empty
    def is_empty(retail_item):
        if(len(retail_item) == 0):
           return True
        else:
           return False

    #assertTrue compare test value with true assert that two object are True
    def test_is_empty_empty_string_success(self):
        result = Test.is_empty("")
        self.assertTrue(result, True)

    #assertFalse compare test value with false
    def test_is_empty_with_string_success(self):
        result = Test.is_empty("retail_item")
        self.assertFalse(result, False)

   
 


