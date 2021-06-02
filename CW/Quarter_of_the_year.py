from math import ceil as c
def quarter_of(month):
    return ( c(month/3) )



print(quarter_of(3), 1)
print(quarter_of(8), 3)
print(quarter_of(11), 4)