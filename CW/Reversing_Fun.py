

def reverse_fun(n,s = ""):
    n = n[::-1]
    s += n[0]
    return s if len(n) == 1 else reverse_fun(n[1:],s)



print(reverse_fun('012345'), '504132')
print(reverse_fun('jointhedarkside'), 'ejdoiisnktrhaed')
