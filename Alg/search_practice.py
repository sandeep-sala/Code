def find_missing(arr):
    n = len(arr)
    return int( ((n+1)*(n+2)/2) - sum(arr) )



p = [1,2,4,5,6]
print(find_missing(p))