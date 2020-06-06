try:
    for _ in range(int(input())):
        n = input()
        k = []
        c = 0
        k.append(n[0])
        for i in range(1,len(n)):
            if n[i] == '>' and k[-1] == '<' and k[-1] != "*":
                c += 1
            k.append(n[i])
        print(c)
except:
    pass