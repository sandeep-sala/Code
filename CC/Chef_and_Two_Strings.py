try:
    for _ in range(int(input())):
        N = str(input())
        M = str(input())
        min,max = 0,0
        for i in range(len(N)):
            if N[i] != M[i] and N[i] != '?' and M[i] != '?':
                min += 1
            elif N[i] != M[i] or N[i] == '?' or M[i] == '?':
                max += 1
        print(str(min)+" "+str(max+min))
except:
    pass