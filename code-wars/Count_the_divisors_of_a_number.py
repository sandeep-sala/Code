def divisors(n):
    return len([i for i in range(1,n+1) if n%i==0])

print(divisors(1), 1) 
print(divisors(4), 3)
print(divisors(5), 2)
print(divisors(12), 6)
print(divisors(30), 8)
print(divisors(4096), 13)