def dig_pow(n, p):
    z = list(map(int, str(n)))
    sum  = 0
    for i,j in enumerate(range( p,p+len(z) )):
        sum +=z[i]**j
    k = sum/n
    if k.is_integer(): return int(k) 
    return -1


print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))