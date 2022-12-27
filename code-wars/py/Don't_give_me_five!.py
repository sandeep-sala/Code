def dont_give_me_five(start, end):
    n = 0
    for i in range(start, end + 1):
        if "5" not in str(i):
            n += 1
    return n


print(dont_give_me_five(1, 9), 8)
print(dont_give_me_five(4, 17), 12)
