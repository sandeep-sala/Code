def parse(data):
    c, l = 0, []
    for i in data:
        if i == "i":
            c += 1
        elif i == "d":
            c -= 1
        elif i == "s":
            c *= c
        elif i == "o":
            l.append(c)
    return l


print(parse("ooo"), [0,0,0])
print(parse("ioioio"), [1,2,3])
print(parse("idoiido"), [0,1])
print(parse("isoisoiso"), [1,4,25])
print(parse("codewars"), [0])
