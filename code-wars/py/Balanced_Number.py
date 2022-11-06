def balanced_num(number):
    ans = "Balanced"
    if number // 10 == 0 or len(str(number // 10)) == 1:
        return ans
    n = list(map(int, str(number)))
    n_len = len(n)
    l,r = 0,0
    if n_len % 2 == 0:
        l,r = (n[:(n_len//2)-1],n[(n_len//2)+1:])
    else:
        l,r = (n[:(n_len//2)],n[(n_len//2)+1:])
    if sum(l) != sum(r):
        return f"Not {ans}"
    return ans


print(balanced_num(7)  , "Balanced");
print(balanced_num(959), "Balanced");
print(balanced_num(13) , "Balanced");
print(balanced_num(432), "Not Balanced");
print(balanced_num(424), "Balanced");
print(balanced_num(1024)    , "Not Balanced")
print(balanced_num(66545)   , "Not Balanced")
print(balanced_num(295591)  , "Not Balanced")
print(balanced_num(1230987) , "Not Balanced")
print(balanced_num(56239814), "Balanced")
