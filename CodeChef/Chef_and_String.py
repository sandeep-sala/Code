try:
    for _ in range(int(input())):
        s = input()
        st = []
        p = 0
        for i in s:
            if len(st) == 0:
                st.append(i)
                continue
            if i == 'x' and st[-1] == 'y' or i == 'y' and st[-1] == 'x':
                st.clear()
                p += 1
        print(p)
except:
    pass
