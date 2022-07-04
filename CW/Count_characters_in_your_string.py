def count(string):
    from collections import Counter
    return dict(Counter(string))

print(count('aba'), {'a': 2, 'b': 1})
print(count(''), {})