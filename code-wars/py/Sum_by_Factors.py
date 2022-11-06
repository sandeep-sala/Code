
def find_prime_facs(n):
    list_of_factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            list_of_factors.append(i)
            n = n/i
            i = i-1
        i += 1
    return set(list_of_factors)


def sum_for_list(lst):
    p_dict = {}
    lst = sorted(lst)

    for i in lst:
        k = find_prime_facs(abs(i))
        if k != {}:
            for j in k:
                if j not in p_dict:
                    p_dict[j] = [i]
                else :
                    p_dict[j].append(i)

    print(p_dict)

    return sorted([  [key,sum(value)]  for key,value in p_dict.items()  ])


a = [12, 15]
print(sum_for_list(a))

a = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]

print(sum_for_list(a))

print([[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158], [107, 107]])