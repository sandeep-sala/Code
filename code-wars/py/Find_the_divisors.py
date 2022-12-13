def divisors(num):
    l = [i for i in range(2,num) if num%i == 0]
    if len(l) == 0:
        return f"{num} is prime"
    return l


print(divisors(15), [3,5])
print(divisors(253), [11,23])
print(divisors(24), [2,3,4,6,8,12])
print(divisors(25), [5])
print(divisors(13), "13 is prime")
print(divisors(3), "3 is prime")
print(divisors(29), "29 is prime")
