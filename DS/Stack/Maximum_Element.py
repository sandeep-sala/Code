stack = []
ma = 0
for _ in range(int(input())):
    p = input()
    if p[0] == '1':
        x = int(p.split()[1])
        if len(stack) == 0 or x > ma:
            ma = x
        stack.append(x)
    elif p == '2':
        stack.pop()
        if len(stack) != 0:
            ma = max(stack)
        else:
            ma = 0
    elif p == '3':
        print(ma)