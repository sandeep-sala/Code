def triple_trouble(one, two, three):
    k = ""
    while len(one)!=0:
        k += one[0] + two[0] + three[0]
        one, two, three = one[1:], two[1:], three[1:]
    return k

def triple_trouble(one, two, three):
    return "".join(a+b+c for a,b,c in zip(one,two,three))


print(triple_trouble("aaa","bbb","ccc"), "abcabcabc")
print(triple_trouble("aaaaaa","bbbbbb","cccccc"), "abcabcabcabcabcabc")
print(triple_trouble("burn", "reds", "roll"), "brrueordlnsl")
print(triple_trouble("Bm", "aa", "tn"), "Batman")
print(triple_trouble("LLh", "euo", "xtr"), "LexLuthor")
