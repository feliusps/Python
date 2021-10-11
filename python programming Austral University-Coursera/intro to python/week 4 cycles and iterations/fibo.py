#fibonnaci number module
def fib(n):  # write the fibonnaci serie up to end
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): #return fibonnaci serie up to end
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b =b, a+b
    return result