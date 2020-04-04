def selectionSort(arr):
    for i in range( 0, len(arr)-1 ):
        min_value = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
        if min_value != i:
            arr[min_value],arr[i] = arr[i],arr[min_value]
    return arr


sorted_list = selectionSort([2,3,0,5,1,3,9])
print(sorted_list)