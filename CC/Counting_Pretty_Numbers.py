try:
    for _ in range(int(input())):
        a, b = input().split()
        print( len( [i for i in range(int(a), int(b)+1) if str(i)[-1] in {'2', '3', '9'} ] ) )
except:
    pass
