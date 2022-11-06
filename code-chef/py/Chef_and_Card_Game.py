try:
    for _ in range(int(input())):
        A,B = 0, 0
        for __ in range(int(input())):
            a,b = map( lambda x : sum(map(int, list(x) )) ,input().split())
            if a == b : 
                A += 1
                B += 1
            else:
                if a < b : B += 1
                if a > b : A += 1
        if A == B:
            print(f'{str(2)} {str(A)}')
        else:
            if A > B : print(f'{str(0)} {str(A)}')
            if A < B : print(f'{str(1)} {str(B)}')

except:
    pass
