def solve_maze(maze):
	sol = [[0 for j in range(len(maze))] for i in range(len(maze))]
	solve_maze_helper(maze, 0, 0, sol)
	for i in sol:
		for j in i:
			print(str(j) + " ", end="")
		print("")


def solve_maze_helper(maze, x, y, sol):
    if x == N - 1 and y == N - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True
    try:
        if x < 0 or x > N or y < 0 or y > N or maze[x][y] != 1:  return False
    except: return False
    sol[x][y] = 1
    for xmov,ymov in [(1, 0), (0, 1)]:
        if solve_maze_helper(maze, x+xmov, y+ymov, sol):
            return True
    sol[y][x] = 0
    return False

if __name__ == "__main__":
    maze = [[1, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1]]
    N = len(maze)
    solve_maze(maze)
