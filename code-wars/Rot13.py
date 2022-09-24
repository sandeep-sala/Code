import string
def rot13(message):
    l = string.ascii_lowercase
    u = string.ascii_uppercase
    p = ""
    for i in message:
        if i in l:
            z = l.index(i) + 13
            if z >= len(l):
               z = z - len(l)
            p += l[z] 
        elif i in u:
            z = u.index(i) + 13
            if z >= len(u):
               z = z - len(u)
            p += u[z]
        else: p += i
    return p





print(rot13(string.ascii_lowercase),"grfg")
print(rot13("Test"),"Grfg")