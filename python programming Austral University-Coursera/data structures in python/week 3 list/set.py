#working with set #printing out no repeated items
set_a = {1, 2, 3, 4, 5}

set_b = {3, 7, 8, 9, 1}

set_c = (set_a ^ set_b) # number in a or b but not in both 
print(set_c)

set_d = (set_a | set_b) #number in a or in b or in both
print(set_d)

set_e = (set_a - set_b) #number in a but not in b
print(set_e)

set_f = (set_a & set_b) # number in a and in b
print(set_f)
print()

#set comprehension
set_g ={'abracadabra'}
set_g = {x for x in 'abracadabra' if x not in 'abc'}
print(set_g)