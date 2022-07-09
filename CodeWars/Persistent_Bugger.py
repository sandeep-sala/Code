
def multiply(n, ac=1):
    ac *= n%10
    if n < 10:
        return ac
    return multiply(n//10, ac)

def persistence(n, ax=0):
    if n < 10:
        return ax
    ax += 1
    return persistence(multiply(n), ax)

print(persistence(39), 3)
print(persistence(4), 0)
print(persistence(25), 2)
print(persistence(999), 4)
