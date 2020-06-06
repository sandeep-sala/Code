import os

# Complete the hourglassSum function below.
def hourglassSum(arr):
    return max([ arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i][j]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1] for i in range(1,len(arr)-1) for j in range(1,len(arr[i])-1 )])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(arr)
    result = hourglassSum(arr)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
"""
00 01 02 03 04           tl = a-1,b-1  , t = a-1,b , tr = a-1,b+1
10 11 12 13 14                           c = a,b
20 21 22 23 24            bl = a+1,b-1  , b = a+1,b  ,br = a+1,b+1

"""