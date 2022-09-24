def factorial(n):
    if n < 0:
        return
    if n in [0,1]:
        return 1
    return n * factorial(n-1)


print(factorial(2) , 2)
print(factorial(0) , 120)
print(factorial(-1), None)