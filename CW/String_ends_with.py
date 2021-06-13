def solution(s, e):
    return  s[len(s)-len(e):] == e


print(solution('abcde', 'cde'), True)
print(solution('abcde', 'abc'), False)
print(solution('abcde', ''), True)