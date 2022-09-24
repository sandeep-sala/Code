def zeros(n):
    k = 0
    n = n//5
    k += n
    while n >= 5:
        n = n//5
        k += n
    return k


print(zeros(0), 0)  # "Testing with n = 0"))
print(zeros(6), 1)  # "Testing with n = 6"))
print(zeros(30), 7) # "Testing with n = 30"))