def same_case(a, b):
    if (a.isupper() and b.isupper()) or (a.islower() and b.islower()):
        return 1
    elif (a.isupper() and b.islower()) or (a.islower() and b.isupper()):
        return 0
    else:
        return -1


print(same_case('C', 'B'), 1)
print(same_case('b', 'a'), 1)
print(same_case('d', 'd'), 1)
print(same_case('A', 's'), 0)
print(same_case('c', 'B'), 0)
print(same_case('b', 'Z'), 0)
print(same_case('\t', 'Z'), -1)
print(same_case('H', ':'), -1)