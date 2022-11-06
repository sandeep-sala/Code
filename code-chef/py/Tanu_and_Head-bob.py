try:
    for _ in range(int(input())):
        n = int(input())
        b = str(input())[:n]
        if 'I' in  b:
            print("INDIAN")
        else:
            if 'Y' in b:
                print("NOT INDIAN")
            else:
                print("NOT SURE")
except:
    pass