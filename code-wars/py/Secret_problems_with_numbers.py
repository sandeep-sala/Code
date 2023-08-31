def secret_number(n):
    return bin(n).count(str(n%2)) ** 2


print(secret_number(2), 4)
print(secret_number(5), 4)
print(secret_number(10), 9)
print(secret_number(15), 16)
print(secret_number(31), 25)
print(secret_number(9978), 36)
print(secret_number(1234567), 121)
print(secret_number(14556237892), 400)
