def nb_year(p0, percent, aug, p,y=0):
    while p0 < p:
        p0 = int(p0 + (p0 * (percent/100)) + aug)
        y += 1
    return y

# print(nb_year(1500, 5, 100, 5000), 15)
print(nb_year(1500000, 0.0, 10000, 2000000), 50)
print(nb_year(1000,2.0,50,1214), 4)


