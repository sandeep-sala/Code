def multiplication_table(size):
    return [[ i*j for j in range(1,size+1)] for i in range(1,size+1)]


print(multiplication_table(3), [[1,2,3],[2,4,6],[3,6,9]])