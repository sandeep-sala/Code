def sort_array(s_a):
    p = sorted([i for i in s_a if i%2 != 0],reverse=True)
    return [ j if j%2==0 else p.pop() for j in s_a ]
    

print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
print(sort_array([]),[])