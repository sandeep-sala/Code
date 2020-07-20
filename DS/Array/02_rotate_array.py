p = [1,2,3,4,5,6,7]

# METHOD 1 (Using temp array)
def m1_Lrotate(arr,d):
    return arr[d:]+ arr[:d]

def m1_Rrotate(arr,d):
    return arr[-d:]+ arr[:-d]

# Method 4 (The Reversal Algorithm)
def m4_Lrotate(arr,d):
    a,b = arr[:d],arr[d:]
    return (a[::-1]+b[::-1])[::-1]

def m4_Rrotate(arr,d):
    arr = arr[::-1]
    a,b = arr[:d],arr[d:]
    return (a[::-1]+b[::-1])

print( m4_Lrotate(p,2) )
print( m4_Rrotate(p,2) )