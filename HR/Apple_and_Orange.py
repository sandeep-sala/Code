def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_count = sum([1 for f in apples if (f+a) >= s and (f+a) <= t])
    b_count = sum([1 for f in oranges if (f+b) >= s and (f+b) <= t])
    print(a_count)
    print(b_count)

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)