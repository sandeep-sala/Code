def solve_nq(n):
	board = [[0 for j in range(n)] for i in range(n)]
	solve_nq_helper(board,0)
	for i in board:
		for j in i:
			print(str(j) + " ", end="")
		print("")

def solve_nq_helper(board, col): 
	if (col >= N): return True
	for i in range(N): 
		if ( (ld[i - col ] != 1 and rd[i + col] != 1)  and cl[i] != 1):
			board[i][col] = 1
			ld[i - col ] = rd[i + col] = cl[i] = 1
			if (solve_nq_helper(board, col + 1)): return True
			board[i][col] = 0
			ld[i - col ] = rd[i + col] = cl[i] = 0
	return False

if __name__ == "__main__":
    N = 4
    ld, rd, cl = [0]*(2*N), [0]*(2*N), [0]*N
    solve_nq(N)
