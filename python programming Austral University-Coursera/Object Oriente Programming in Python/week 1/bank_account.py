"""
For this challenge, create a bank account class that has two attributes:
.owner
.balance

and two methods:

.deposit
.withdraw

As an added requirement, withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, 
and test to make sure the account can't be overdrawn.
"""

class Account:

      def __init__(self,  owner, balance):
          #two attributes  
          self.owner = owner
          self.balance = balance

      def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

      #two methods

      def deposit(self, deposit_amount):
          self.balance += deposit_amount
          print('Deposit Accepted')

      def withdraw(self, withdraw_ammount):
          if self.balance >= withdraw_ammount:
                self.balance -= withdraw_ammount
                print('Withdraw Accepted')
          else:
              print('Insufficient Funds')


# 1. Instantiate the class
acct1 = Account('Felix',1000)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
acct1.owner

# 4. Show the account balance attribute
print("Account Balance %.2f " %(acct1.balance))

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(2000)