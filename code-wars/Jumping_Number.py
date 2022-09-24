def jumping_number(n):
    ans = ["Jumping!!","Not!!"]
    mw = str(n)
    if len(mw) == 1:
        return ans[0]
    p = mw[0]
    for i in mw[1:]:
        if eval(f"{i}-{p}") in [1,-1]:
            p = i
        else:
            return ans[1]
    return ans[0]

print(jumping_number(1), "Jumping!!")
print(jumping_number(7), "Jumping!!")
print(jumping_number(9), "Jumping!!")
print(jumping_number(23), "Jumping!!")
print(jumping_number(32), "Jumping!!")
print(jumping_number(79), "Not!!")
print(jumping_number(98), "Jumping!!")
print(jumping_number(8987)    , "Jumping!!")
print(jumping_number(4343456) , "Jumping!!")
print(jumping_number(98789876), "Jumping!!")
