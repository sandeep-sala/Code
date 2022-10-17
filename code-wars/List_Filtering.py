def filter_list(l):
    return [i  for i in l if type(i)==int]


print(filter_list([1, 2, 'a', 'b']), [1, 2], 'For input [1, 2, "a", "b"]')
print(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15], 'Fot input [1, "a", "b", 0, 15]')
print(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123], 'For input [1, 2, "aasf", "1", "123", 123]')