MOVES = [
    (1,2), #1 Top Right
    (2,1), #2 Right Top
    (2,-1), #3 Right Bottom
    (1,-2), #4 Bottom Right
    (-1,-2), #5 Bottom Left
    (-2,-1), #6 Left Bottom
    (-2,1), #7 Left Top
    (-1,2), #8 Top Left
]

def solve_knights_tour(n,x,y):
    board = [[-1 for i in range(n)]for j in range(n)]
    solve_knights_tour_helper(n,board,x,y,0)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def solve_knights_tour_helper(n,board,x,y,count):
    if count == n*n: return True
    if (x<0) or (x>=n) or (y<0) or (y>=n) or board[x][y] != -1: return False
    board[x][y] = count
    for xmov,ymov in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
        if solve_knights_tour_helper(n,board,x+xmov,y+ymov,count+1):
            return True
    board[x][y] = -1
    return False


solve_knights_tour(8,0,0)
