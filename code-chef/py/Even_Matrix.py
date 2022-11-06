try:
    for _ in range(int(input())):
        n = int(input())
        c = ''
        l = n**2
        F = n%2 == 0
        if F:
            k = 1
            for i in range(1,n+1):
                a = []
                for j in range(n):
                    a.append(str(k))
                    k += 1
                if i%2 !=0:
                    c += ' '.join(a)+'\n'
                else:
                    c += ' '.join(a[::-1])+'\n'
        else:
            for i in range(1,l+1):
                c += str(i)+'\n' if i%n == 0 else str(i)+' '
        print(c[:-1])
except:
    pass