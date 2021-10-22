try:
    for _ in range(int(input())):
        x,y = map( int, input().split())
        s = input()
        print(  (x*(s.count("1"))) +(y * len(max(s.split("0")))))
except:
    pass