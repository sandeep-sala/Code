try:
    for _ in range(int(input())):
        n = str(input())
        print( abs(max(n.count("a"),n.count("b")) - len(n) ))
except:
    pass