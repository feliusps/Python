
"""program a cash register for a warehouse.
 The system must be able to scan a product (the cashier can type in the product code), 
 and add it to the list of products purchased for that customer.
 It should also show the subtotal. The cashier can finish the purchase whenever
 he wishes and the system must apply the corresponding discounts to the products.
 Then, the cashier indicates how much the customer pays with and the system must 
 show the change to be returned to the customer. do the models and 
 tests of the functionalities. It is not necessary to make a graphical interface
 (or console), but the whole operation can be validated with the unit tests."""

 #import retail and cash_register classes


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

