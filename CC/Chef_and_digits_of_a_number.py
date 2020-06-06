try:
    for _ in range(int(input())):
        n = str(input())
        if (  len(n)-n.count("1") == 1 )or ( len(n)-n.count("0") == 1) :
            print("Yes")
        else:
            print("No")
except:
    pass