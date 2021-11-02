"""program a cash register for a warehouse.
 The system must be able to scan a product (the cashier can type in the product code), 
 and add it to the list of products purchased for that customer.
 It should also show the subtotal. The cashier can finish the purchase whenever
 he wishes and the system must apply the corresponding discounts to the products.
 Then, the cashier indicates how much the customer pays with and the system must 
 show the change to be returned to the customer. do the models and 
 tests of the functionalities. It is not necessary to make a graphical interface
 (or console), but the whole operation can be validated with the unit tests."""

#we will use class cashRegister from cash_register.py and class reatailtem from retail.py 
#main to test the program

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
#******* TESTING CASH REGISTER *******
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


import unittest
#test cases are represented by unittest.TestCase instances.
class RetailItem:
    def __init__(self, description, inventory, price):
        self.__description = description
        self.__inventory = inventory
        self.__price = price
    
    def set_description(self, description):
        self.__description = description
    
    #inventary level
    def set_inventory(self, inventory):
        self.__inventory = inventory
    
    #put the price
    def set_price(self, price):
        self.__price = price
    
    #get the item description
    def get_description(self):
        return self.__description
    
    #check for inventary
    def get_inventory(self):
        return self.__inventory
    
    #get the item price
    def get_price(self):
        return self.__price
    
    def __str__(self):
        result = 'Description: ' + self.get_description() + '\n' + \
                 'Units in inventory: ' + str(self.get_inventory()) + \
                 '\nPrice: $' + str(self.get_price())
        return result

#=========================================================
#*******TESTING RETAIL ITEMS ********
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

#import retail and cash_register classes
#==============================================
#********MAIN TO TEST THE PROGRAM*********
#==============================================

import retail
import cash_register

# constants to hold the options of purchase items
ITEM1 = 1
ITEM2 = 2
ITEM3 = 3
ITEM4 = 4
ITEM5 = 5

def main():
#create sale items
    Item1 = retail.RetailItem("Item1", 10, (19.99 - (19.99 *.1) )) #10 percent discount
    Item2 = retail.RetailItem("Item2", 15, 12.50)  # not discount
    Item3 = retail.RetailItem("Item3", 3, 79.00 - (79.00 * 0.15 ))  #15% discount
    Item4 = retail.RetailItem("Item4", 50, 1.00) #not discount
    Item5 = retail.RetailItem("Item5", 5, 49.99 - (49.99 * 0.1)) #10% disccount

# create dictionary of sale items
    sale_items = {ITEM1:Item1, ITEM2:Item2, ITEM3:Item3, ITEM4:Item4, ITEM5:Item5}

# create a cash register
    register = cash_register.CashRegister()

# initialize loop test
    checkout = 'N'

# user wants to purchase more items
    while checkout=='N':
        user_choice = get_user_choice()
        item = sale_items[user_choice]
        if item.get_inventory() == 0:
            print("The item is out of stock.")
        else:
            register.purchase_item(item)
# update item
            new_item = retail.RetailItem(item.get_description(), item.get_inventory()-1,\
                                         item.get_price())

            sale_items[user_choice] = new_item
            checkout = input("Are you ready to check out (Y/N)? ")
    print()
    print("Your purchase total is: ", format(register.get_total(), '.2f'))
    print()
    register.show_items()
    register.clear()

def get_user_choice():
    print("Menu")
    print("---------------------------------")
    print("1. Item1")
    print("2. Item2")
    print("3. Item3")
    print("4. Item4")
    print("5. Item5")
    print()
 
    choice = int(input("Enter the menu number of the item " +\
                 "you would like to purchase: "))
    print()
    while choice > ITEM5 or choice < ITEM1:
          choice = int(input("Please enter a valid item number: "))
          print()
    return choice
main()

