def no_boring_zeros(n):
    if n == 0:
        return n
    n = str(n)
    while True:
        if n[-1] == "0":
            n = n[:-1]
        else:
            return int(n)


def no_boring_zeros(n):
    return int(str(n).strip('0') or 0)

print(no_boring_zeros(1450), 145)
print(no_boring_zeros(960000), 96)
print(no_boring_zeros(1050), 105)
print(no_boring_zeros(-1050), -105)
print(no_boring_zeros(0), 0)
print(no_boring_zeros(2016), 2016)