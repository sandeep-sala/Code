def some_but_not_all(seq, pred): 
    return True if 0<list( map(pred, seq) ).count(True)<len(seq) else False

print(some_but_not_all('abcdefg&%$', str.isalpha), True)
print(some_but_not_all('&%$=', str.isalpha), False)
print(some_but_not_all('abcdefg', str.isalpha), False)
print(some_but_not_all([4, 1], lambda x: x>3), True)
print(some_but_not_all([1, 1], lambda x: x>3), False)
print(some_but_not_all([4, 4], lambda x: x>3), False)