#model a currency quantity able to represent any currency and 
# make mathematics operation with the currency - + * /


#class to represent  a currency

class Currency(object):
    
    def __init__(self, name, symbol, factor):
        self.name = name
        self.symbol = symbol
        self.factor = factor

    def convert_amount_to_base_currecy(self, aNumber):
        return aNumber * self.factor

    def convert_amount_from_base_currency(self, aNumber):
        return aNumber / self.name

    def __repr__(self):
        return self.name

#class to represent  amount of money
class Money(object):

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def base_currency_amount(self):
        return self.currency.convert_amount_to_base_currency(self.amount)

    def __add__(self, anAmountOfMoney):
        amount = self.base_currency_amount() + anAmountOfMoney.base_currency_amount()
        amount = self.currency.convert_amount_from_base_currency(amount)
        return Money(amount, self.currency)

    def __sub__(self, anAmountOfMoney):
        amount = self.base_currency_amount() - anAmountOfMoney.base_currency_amount()
        amount = self.currency.convert_amount_from_base_currency(amount)
        return Money(amount, self.currency)

    def __mul__(self, aNumber):
       return Money(self.amount * aNumber, self.currency)

    def __truediv__(self, aNumber):
        return Money(self.amount / aNumber, self.currency)


    def __repr__(self):
        return '{} {}'.format(self.currency.symbol, self.amount)

    

dollar = Currency('dollar', 'US$', 1)
pesos = Currency('pesos (Arg)', '$', 1/40)

one_dollar = Money(1, dollar)
one_peso = Money(1, pesos)


       

