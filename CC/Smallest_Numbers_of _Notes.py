try:
    for _ in range(int(input())):
        n = int( input() )
        m = 0
        if n%100 != n:
            m += n //100
            n = n%100
        if n%50 != n: 
            m += n //50
            n = n%50
        if n%10 != n:
            m += n //10
            n = n%10
        if n%5 != n:
            m += n //5
            n = n%5
        if n%2 != n:
            m += n //2
            n = n%2
        if n%1 != n:
            m += n //1
            n = n%1
        print(m)
except:
    pass