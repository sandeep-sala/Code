
def l_wrap(l):
    n, i = [0,], 1
    while (n[-1] + i) < l:
        n.append(n[-1] + i)
        i += 1
    return n[1:][::2]

def tops(msg):
    return "".join([ msg[i]for i in l_wrap(len(msg))[::-1]])


# print(tops(""),"")
# print(tops("12"),"2")
print(tops("abcdefghijklmnopqrstuvwxyz12345"),"3pgb")
# print(tops("abcdefghijklmnopqrstuvwxyz1236789ABCDEFGHIJKLMN"),"M3pgb")