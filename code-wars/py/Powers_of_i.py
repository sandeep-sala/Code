def pofi(n):
    return ['1','i','-1','-i'][n%4]

print(pofi(0),'1')
print(pofi(1),'i')
print(pofi(2),'-1')
print(pofi(3),'-i')

print(pofi(4),'1')
print(pofi(5),'i')
print(pofi(6),'-1')
print(pofi(7),'-i')

print(pofi(8),'1')
print(pofi(9),'i')
print(pofi(10),'-1')
