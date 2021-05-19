try:
    solve = lambda x: x[0]*x[2] + x[1]*x[3]
    print(solve(list(map( int ,input().split() ))))
except Exception as e:
    print(e)
