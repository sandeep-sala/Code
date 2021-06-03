def first(seq, n=1): 
    return seq[:n]


seq = ['a', 'b', 'c', 'd', 'e']
print(first(seq), ['a'])
print(first(seq, 0), []);
print(first(seq, 1), ['a']);
print(first(seq, 2), ['a', 'b']);
print(first(seq, 10), ['a', 'b', 'c', 'd', 'e'])