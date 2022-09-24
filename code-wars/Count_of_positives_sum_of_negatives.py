def count_positives_sum_negatives(arr):
    a,b = [],[]
    for i in arr:
        if i > 0 :
            a.append(i)
        elif i < 0 :
            b.append(i)
    return [] if arr == [] else [len(a),sum(b)]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
print(count_positives_sum_negatives([1]),[1,0])
print(count_positives_sum_negatives([-1]),[0,-1])
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
print(count_positives_sum_negatives([-61, -3, 84, 4, 76, 41, 9, 18, -49, -17, 52, -37, 93, 86, 90, -90, 47, -75, 8, -13, -63, 32, -78, 74, 91, -13, 71, 99, -19, 9, 100, -47, 65, 13, 92, -74, 31, 36, -35, 91, 47, 25, 28, 87, -75, 72, 95, -31, -3, 10, -25, -93, -100, -89, -11, -27, 63, 96, -36, 3]),[35, -1164])