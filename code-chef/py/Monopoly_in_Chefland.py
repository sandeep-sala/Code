def monopolistic(a, b, c):
    return "YES" if (a > b + c) or (b > a + c) or (c > a + b) else "NO"


if __name__ == "__main__":
    for __ in range(int(input())):
        a, b, c = list(map(int,input().split()))
        print(monopolistic(a, b, c))
