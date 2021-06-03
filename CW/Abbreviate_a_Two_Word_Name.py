def abbrev_name(name):
    return ".".join(list(map(lambda a:a[0].upper() ,name.split(" "))))



print(abbrev_name("Sam Harris"), "S.H")
print(abbrev_name("Patrick Feenan"), "P.F")
print(abbrev_name("Evan Cole"), "E.C")
print(abbrev_name("P Favuzzi"), "P.F")
print(abbrev_name("David Mendieta"), "D.M")