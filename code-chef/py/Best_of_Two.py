def best_od_two(a, b):
    return max(a, b)


if __name__ == "__main__":
    for __ in range(int(input())):
        a, b = list(map(int,input().split()))
        print(best_od_two(a, b))
