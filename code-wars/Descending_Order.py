def descending_order(num):
    return int("".join(sorted(list(str(num)), reverse=True)))


print(descending_order(0), 0)
print(descending_order(1), 1)
print(descending_order(111), 111)
print(descending_order(15), 51)
print(descending_order(1021), 2110)
print(descending_order(123456789), 987654321)
