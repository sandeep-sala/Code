def cheaper_cab(x, y):
    return "ANY" if (x == y) else "FIRST" if (x < y) else "SECOND"

if __name__ == "__main__":
    for __ in range(int(input())):
        x, y = list(map(int,input().split()))
        print(cheaper_cab(x, y))
