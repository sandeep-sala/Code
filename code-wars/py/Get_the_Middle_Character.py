def get_middle(s):
    l = len(s)
    m = (l//2)
    if l%2==0:
        pass
        return s[m-1:m+1]
    else:
        return s[m]


print(get_middle("test"),"es")
print(get_middle("testing"),"t")
print(get_middle("middle"),"dd")
print(get_middle("A"),"A")
print(get_middle("of"),"of")