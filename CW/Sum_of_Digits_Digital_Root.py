def digital_root(n):
    n = sum(list(map(int, str(n).strip())))
    if len(str(n)) == 1:
        return n
    return digital_root(n)
        


print(digital_root(16), 7)
print(digital_root(942), 6)
print(digital_root(132189), 6)
print(digital_root(493193), 2)