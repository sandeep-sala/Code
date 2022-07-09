def valid_parentheses(n):
    s = []
    n = n.strip()
    for i in n:
        if i == "(":
            s.append(i)
        elif i == ")":
            if len(s) == 0 : return False
            elif "(" == s[-1] : 
                s.pop()
    if len(s) == 0: return True
    return False



print(valid_parentheses("  ("),False)
print(valid_parentheses(")test"),False)
print(valid_parentheses(""),True)
print(valid_parentheses("hi())("),False)
print(valid_parentheses("hi(hi)()"),True)