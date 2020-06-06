try:
    n = list(str(input()))
    for _ in range(int(input())):
        s = list(str(input()))
        for i in s:
            if i in n:
                k = "Yes"
            else:
                k = "No"
                break
        print(k) 
except:
    pass