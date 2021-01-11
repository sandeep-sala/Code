def get_sum(a,b):
    return sum( [i for i in range( min(a,b) , (max(a,b)+1) )])

print(get_sum(0,1),1)
print(get_sum(0,-1),-1)