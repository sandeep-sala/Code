def stock_list(b, c):
    d = {}
    for i in b:
        if i[0] in d:
            d[i[0]] += int(i.split()[-1])
        else:
            d[i[0]] = int(i.split()[-1])

    return " - ".join([f"({i} : {d.get(i,0)})" for i in c])


b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "C", "D"]
print(stock_list(b, c), "(A : 0) - (B : 1290) - (C : 515) - (D : 600)")

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c), "(A : 200) - (B : 1140)")
