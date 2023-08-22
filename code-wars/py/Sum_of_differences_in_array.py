def sum_of_differences(arr):
    arr = sorted(arr, reverse=True)
    k = len(arr)-1
    i,j,s = 0,1,0
    while j <= k:
        s+=(arr[i]-arr[j])
        i+=1
        j+=1
    return s


print(sum_of_differences([1, 2, 10]), 9)
print(sum_of_differences([-3, -2, -1]), 2)
print(sum_of_differences([1, 1, 1, 1, 1]), 0)
print(sum_of_differences([-17, 17]), 34)      
print(sum_of_differences([]), 0)
print(sum_of_differences([0]), 0)
print(sum_of_differences([-1]), 0)
print(sum_of_differences([1]), 0)