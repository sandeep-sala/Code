def permutations(ini_str):
    from itertools import permutations 
    return list({''.join(p) for p in permutations(ini_str)})


print(sorted(permutations('a')), ['a'])
print(sorted(permutations('ab')), ['ab', 'ba'])
print(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])