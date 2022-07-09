def find_missing_letter(chars):
    a = ord(chars.pop())
    while chars:
        b = ord(chars.pop())
        if abs(b-a) > 1:
            return chr(a-1)
        else:
            a = b
    return ''

print(find_missing_letter(['a','b','c','d','f']), 'e')
print(find_missing_letter(['O','Q','R','S']), 'P')

