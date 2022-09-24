def tidyNumber(n):
    n = list(str(n))
    for i, j in enumerate(n):
        if i == 0:
            continue
        if int(n[i-1]) > int(j) :
            return False
    return True


print(tidyNumber(12), True)
print(tidyNumber(102), False)
print(tidyNumber(9672), False)
print(tidyNumber(2789), True)