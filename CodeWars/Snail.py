def snail(snail_map):
    N = len(snail_map)
    top, bottom, left, right = 0, N-1, 0, N-1
    direction = 0
    snail = []
    if N == 1:
        if snail_map[0] == []:
            return []
    while( top<=bottom and left<=right ):
        if direction == 0:
            for i in range(left,right+1):
                snail.append(snail_map[top][i])
            top += 1
        elif direction == 1:
            for i in range(top,bottom+1):
                snail.append(snail_map[i][right])
            right -= 1
        elif direction == 2:
            for i in range(right,left-1,-1):
                snail.append(snail_map[bottom][i])
            bottom -= 1
        elif direction == 3:
            for i in range(bottom,top-1,-1):
                snail.append(snail_map[i][left])
            left += 1
        direction = (direction+1)%4
    return snail


array = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
         ]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
# print(snail(array), expected)
print(snail(array))


array = [[0, 0],
         [0, 0]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(snail(array), expected)
print(snail(array))
