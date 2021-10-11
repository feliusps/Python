#list operation

#1. define a list variable 

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a_list)

#2. slicing From that list, overwrite the variable with the sublist 
#   from the second element to the eighth element inclusive.

a_list[1:8]
print(a_list)


#3. add 9 to the lis
a_list.append(9)
print(a_list)

#4. add 5 to the beginnint of the list
a_list.insert(0, 5)
print(a_list)


#5. delete the first number 5
a_list.remove(5)
print(a_list)


#6. remove last item of the list
a_list.pop()
print(a_list)


