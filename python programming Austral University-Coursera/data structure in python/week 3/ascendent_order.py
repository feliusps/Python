#ordering sum of even numbers
#Sort the list in place according to the sum of the numbers in each tuple. 
# That is, if x is an element of the list, sort by x [0] + x [1].
#  In Ascending order, example 
# the ordered list is: [(1, 3), (2, 3), (4, 1), (1, 5), (5, 2), (6, 2)]

#order the following list
a_list = [(6, 2), (1, 5), (2, 3), (4, 1), (5, 2), (1, 3)] 
x = []
#using list comprehention

print(a_list.sort(key = x[0] + x[1]))