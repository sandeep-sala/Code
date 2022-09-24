try:
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.remove(max(a))
        b.remove(max(b))
        a,b = sum(a),sum(b)
        if(a<b):
            print('Alice')
        elif(a>b):
            print('Bob')
        elif(a==b):
            print('Draw')
except:
    pass