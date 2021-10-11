
#1. generate even number between n = 1 until n = 100 inclusiveusing list comprehension


list_comprehension = [x for x in range(1, 101) if (x % 2) == 0]
#print(list_comprehension)

#2. which expression get the same result using list comprehension

cuadrados = []

for x in range(10):

    cuadrados.append(x**2)

#print(cuadrados)

#option a
cuadrado_a = [x**2 for x in range(10)]
#print(cuadrado_a)

#option b
cuadrado_b = list(map(lambda x:x**2, range(10)))
#print(cuadrado_b)

#3. which codes create a list = a_list = [1, 3, 5, 7, 9]

a_list = [x for x in range(10) if x % 2 == 1]
#print(a_list)

#4. what the nest expression return
list_expression = [x*y for x in [1,2,3] for y in [3,1,4] if x != y]
print(list_expression)