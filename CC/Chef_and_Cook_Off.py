try:
    for _ in range(int(input())):
        p = list( map(int,input().split()) )
        k = p.count(1)
        if k == 0:
            print("Beginner")
        if k == 1:
            print("Junior Developer")
        if k == 2:
            print("Middle Developer")
        if k == 3:
            print("Senior Developer")
        if k == 4:
            print("Hacker")
        if k == 5:
            print("Jeff Dean")
except:
    pass