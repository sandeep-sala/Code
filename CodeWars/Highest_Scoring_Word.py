def high(x):
    w_list = [ (sum([ ord(i)-96 for i in word.strip()]),word) for word in x.split(" ") ]
    mx = w_list[0]
    for i in w_list[1:]:
        if mx[0] < i[0]:
            mx = i
    return mx[1]


print(high('man i need a taxi up to ubud'), 'taxi')
print(high('what time are we climbing up the volcano'), 'volcano')
print(high('take me to semynak'), 'semynak')
print(high('aa b'), 'aa')
print(high('b aa'), 'b')
print(high('bb d'), 'bb')
print(high('d bb'), 'd')
print(high("aaa b"), "aaa")