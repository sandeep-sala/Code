def isinRange(board):
    return all([ True if (1<=j<=9) else False for i in board for j in i   ] )

def isuniqueRow(board):
    return all([ True  if len(set(row)) == 9 else False  for row in board ] )

def isuniqueCol(board):
    return all([ True if len(set([ board[j][i] for j in range(0, 9)])) == 9 else False for i in range(0, 9)])

def isuniqueSubMatrix(board):
    return all([True if len(set([ board[i+k][j+l] for l in range(0, 3) for k in range(0, 3) ])) == 9 else False for j in range(0, 9 - 2, 3) for i in range(0, 9 - 2, 3)])

def valid_solution(board):
    if not isinRange(board): return False
    return all([isuniqueRow(board),isuniqueCol(board),isuniqueSubMatrix(board)])

print(valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2], 
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True)

print(valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2], 
    [6, 7, 2, 1, 9, 0, 3, 4, 9],
    [1, 0, 0, 3, 4, 2, 5, 6, 0],
    [8, 5, 9, 7, 6, 1, 0, 2, 0],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 0, 1, 5, 3, 7, 2, 1, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False)