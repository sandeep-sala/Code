def str_count(strng, letter):
    return strng.count(letter)

print(str_count('hello', 'l'), 2)
print(str_count('hello', 'e'), 1)
print(str_count('codewars', 'c'), 1)
print(str_count('ggggg', 'g'), 5)
print(str_count('hello world', 'o'), 2)
print(str_count('', 'z'), 0)