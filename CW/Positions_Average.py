from itertools import permutations as pm


def count_common(a, l):
    c = 0
    for i in range(l):
        if a[0][i] == a[1][i]:
            c += 1
    return c


def pos_average(s):
    L = s.split(", ")
    ln = len(L[0])
    c, k = 0, 0
    for i in list(pm(L, 2)):
        c += count_common(i, ln)
        k += 1
    return (c/(k*ln))*100


print(
    pos_average(
        "466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"
    ),
    26.6666666667,
)
print(
    pos_average(
        "444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490"
    ),
    29.2592592593,
)

