#python generators practice

#create a funcion that generate even numbers
def numeros_pares(n):
    return (x for x in range(n) if x % 2 == 0)


    
gen = numeros_pares(15)

gen.__next__()

gen.__next__()

print(list(gen))