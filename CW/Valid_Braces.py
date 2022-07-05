def valid_braces(n):
    paren_dict = {
        "(":")",
        "{":"}",
        "[":"]"
    }
    s = []
    n = n.strip()
    for i in n:
        if i in paren_dict:
            s.append(i)
        else:
            if len(s) == 0 : return False
            elif paren_dict[s[-1]] == i:
                s.pop()
    if len(s) == 0: return True
    return False


print(valid_braces( "()" ),True)
print(valid_braces( "(}" ),False)
print(valid_braces( "[]" ),True)
print(valid_braces("[(])"),False)
print(valid_braces( "{}" ),True)
print(valid_braces( "{}()[]" ),True)
print(valid_braces( "([{}])" ),True)
print(valid_braces( "([}{])" ),False)
print(valid_braces( "{}({})[]" ),True)
print(valid_braces( "(({{[[]]}}))" ),True)
print(valid_braces( "(((({{" ),False)
print(valid_braces( ")(}{][" ),False)
print(valid_braces( "())({}}{()][][" ),False)