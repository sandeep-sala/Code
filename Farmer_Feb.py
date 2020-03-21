try:
    def prime(n) :
        flag = 0
        for i in range (2 , n//2+1) :
            if(n % i == 0):
                flag = 1
        if (flag == 0 ):
            return True
        else :
            return False

    for _ in range(int(input())):
        s = sum(map(int,  input().split()))
        i = 1
        while(True):
            if(prime(s+ i)):
                print(i)
                break
            else :
                i += 1
except:
    pass
