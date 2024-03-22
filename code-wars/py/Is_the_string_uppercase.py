def is_uppercase(inp):
    p = all(True if i.isupper() else False for i in inp.split())
    return inp.isupper()


print(is_uppercase("c"), False)
print(is_uppercase("C"), True)
print(is_uppercase("hello I AM DONALD"), False)
print(is_uppercase("HELLO I AM DONALD"), True)
print(is_uppercase("$%&"), True)
