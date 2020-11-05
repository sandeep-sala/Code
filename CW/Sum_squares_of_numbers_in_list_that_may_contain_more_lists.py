def sumsquares(l):
    sum  = 0
    if not isinstance(l,list):
        return l*l
    else:
        for i in l:
            sum += sumsquares(i)
    return sum


l = [1,2,3]
print(sumsquares(l),14)
l = [[1,2],3]
print(sumsquares(l),14)
l = [[[[[[[[[1]]]]]]]]]
print(sumsquares(l),1)
l = [10,[[10],10],[10]]
print(sumsquares(l),400)
l = [1,[[3],10,5,[2,[3],[4],[5,[6]]]],[10]]
print(sumsquares(l),325)