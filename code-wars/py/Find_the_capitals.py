import string


def capitals(word):
    p = []
    for i, j in enumerate(word):
        if j in string.ascii_uppercase:
            p.append(i)
    return p


print(capitals("CodEWaRs"), [0, 3, 4, 6])
