def rev_sub(arr):
    l,k = [],[]
    for i in range(len(arr)):
        if arr[i]%2==0:
            k.insert(0,arr[i])
        else:
            if k:
                l+=k
                k = []
            l.append(arr[i])
    return l+k


print(rev_sub([]), [])
print(rev_sub([4, 2]), [2, 4])
print(rev_sub([2, 4, 3]), [4, 2, 3])
print(rev_sub([2, 4, 3, 10, 2]), [4, 2, 3, 2, 10])
