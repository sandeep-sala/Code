def nb_dig(n, d):
    return "".join([str(i * i) for i in range(n + 1)]).count(str(d))



print(nb_dig(5750, 0), 4700)
print(nb_dig(11011, 2), 9481)
print(nb_dig(12224, 8), 7733)
print(nb_dig(11549, 1), 11905)
