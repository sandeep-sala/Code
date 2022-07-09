try:
    
    for _ in range(  int(input()) ):
        k = int(input())
        c = 64 - k
        ans=[['.' for i in range(8)] for j in range(8)]
        ans[7][7]='O'
        for i in range(8):
            for j in range(8):
                if c > 0:
                    ans[i][j] = 'X'
                    c-=1
        for i in range(8):
            print("".join(ans[i]))
except:
    pass