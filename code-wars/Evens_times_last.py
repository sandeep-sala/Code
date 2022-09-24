def even_last(n):
    return  sum([n[i] for i in range(0,len(n),2) ])*n[-1] if n else 0


print(even_last([2, 3, 4, 5]), 30)
print(even_last([]), 0)