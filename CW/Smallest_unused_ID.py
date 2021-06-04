def next_id(arr):
    for i in range( len(arr)+1 ):
        if i not in arr: return i
    return max(arr)+1

print(next_id([0,1,2,3,4,5,6,7,8,9,10]), 11)
print(next_id([5,4,3,2,1]), 0)
print(next_id([0,1,2,3,5]), 4)
print(next_id([0,0,0,0,0,0]), 1)
print(next_id([]), 0)
print(next_id([0,0,1,1,2,2]), 3)
print(next_id([0,1,1,1,3,2]), 4)
print(next_id([0,1,0,2,0,3]), 4)
print(next_id([9,8,0,1,7,6]), 2)
print(next_id([9,8,7,6,5,4]), 0)