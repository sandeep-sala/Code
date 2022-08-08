def is_eureka(n):
    if len(n) > 1:
        t = []
        for i, j in enumerate(n):
            try:
                t.append(int(j)**(i+1))
            except:
                pass
        p = str(sum(t))
        return n == p
    else:
        return True

def sum_dig_pow(a, b):
    return [ i for i in range(a,b+1) if is_eureka( str(i) ) ]

print(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
print(sum_dig_pow(10, 89),  [89])
print(sum_dig_pow(10, 100),  [89])
print(sum_dig_pow(90, 100), [])
print(sum_dig_pow(89, 135), [89, 135])