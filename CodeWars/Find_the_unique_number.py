def find_uniq(arr):
    for i in set(arr):
        if arr.count(i) == 1:
            return i
    return i



print(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
print(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
print(find_uniq([ 3, 10, 3, 3, 3 ]), 10)