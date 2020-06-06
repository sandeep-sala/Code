try:
    T, S = input().split()
    D, i = {}, 97
    for j in S:
        D[chr(i)] = j
        i += 1
    for _ in range(int(T)):
        p = input()
        k = ""
        for i in p:
            if i == "_":
                k += " "
            elif i.lower() in D:
                if i.isupper() == True:
                    k += D[i.lower()].upper()
                else:
                    k += D[i]
            else:
                k += i
        print(k)
except:
    pass
