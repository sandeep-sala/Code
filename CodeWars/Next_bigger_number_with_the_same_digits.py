def next_bigger(n):
    mx = lambda n : int("".join(sorted(list(str(n)),reverse=True)))
    maxx = mx(n)
    for i in range(n+1,maxx+1):
        if(mx(i)==maxx):
            return i
    return -1


print(next_bigger(1234567890), 1234567908)
print(next_bigger(2017), 2071)
print(next_bigger(414), 441)
print(next_bigger(144), 414)