"""greengrocer gave us their price list per kilo. 
create the dictionary with the price list:"""

prices = {'apple': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pear': 3.75, 'plum': 2.45, 'peach': 4.55, 'melon': 7.35, 'watermelon': 9.70 , 'anana': 11.25}

#If we have the following list for a purchase:  which id the total cost of the list
#2 kg of apples
#2.5 kg of banana
#1 kg of kiwi
#3 kg of pear
#1 kg of plums
#2 kg of peach
#5 kg of melón
#10 kg of watermelon
#3 kg of pineapple

quantity = {'apple': 2.0, 'banana': 2.0, 'kiwi': 1.0, 'pear': 3.0, 'plum': 1.0, 'peach': 2.0, 'melon': 5.0, 'watermelon': 10.0 , 'anana': 3.0}#quantity key-value
quantity['mango']

#using dictionary comprehension + key
cost= {key: quantity[key] * prices.get(key, 0) for key in quantity.keys()}
print(cost)
total_cost = sum(cost.values())
print("the total cost of the fuits is : ",  str(total_cost))