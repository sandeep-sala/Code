def solution(args):
    p = []
    l = len(args)
    i,j = 0,0
    while j < l:
        try:
            if abs(args[i] - args[i+1]) == 1 and abs(args[i+1] - args[i+2]) == 1:
                j += 2
        except:
            pass
        if i != j:
            while j < l-1:
                if abs(args[j] - args[j+1]) == 1:
                    j += 1
                else:
                    break
        
        j += 1
        k = args[i:j]
        if len(k) == 1:
            p.append(f"{k[0]}")
        else:
            p.append(f"{k[0]}-{k[-1]}")
        i = j
    return ",".join(p)


print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
print(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')