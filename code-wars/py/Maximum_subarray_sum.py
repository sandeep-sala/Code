def max_sequence(L):
    if len(L) == 0 : 
        return 0
    else:
        p = max({  sum(L[i:i+j]) for i in range(0,len(L))  for j in range(1, len(L)-i+1 ) })
        return p if p >= 0 else 0


print(max_sequence([]), 0)
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
