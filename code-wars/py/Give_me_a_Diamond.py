def diamond(n):
    if n < 0 or n%2 == 0:
        return
    k = ""
    for j,i in enumerate(range(n,0,-2)):
        if i == n:
            k = "*"*i+"\n"
        else:
            k = " "*j+"*"*i+"\n" + k + " "*j+"*"*i+"\n"
    return k

expected =  " *\n"
expected += "***\n"
expected += " *\n"
print(diamond(1) == "*\n")
print(diamond(2) == None)
print(diamond(3) == expected)
print(diamond(5) == "  *\n ***\n*****\n ***\n  *\n")
print(diamond(0) == None)
print(diamond(-3) == None)