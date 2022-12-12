import itertools 

def is_defended(attackers, defenders):
    l,w = 0,0
    for i,j in itertools.zip_longest(attackers, defenders):
        i = i or 0
        j = j or 0
        if i > j:
            l += 1
        elif i < j:
            w += 1
    if l > w:
        return False
    elif l < w:
        return True
    else:
        l,w = sum(attackers),sum(defenders)
        if l > w:
            return False
        elif l < w:
            return True
        else:
            return True
    return False


print(is_defended([ 2, 9, 9, 7 ], [ 1, 1, 3, 8]), False)
print(is_defended([1,3,5,7], [2,4,6,8]), True)
print(is_defended([10, 10, 1, 1], [4, 4, 7, 7]), True)
print(is_defended([], [1,2,3]), True)
print(is_defended([1,2,3], []), False)
