def solution(s):
    return "".join([f" {i}" if i.isupper() else i for i in s])


print(solution("helloWorld"), "hello World")
print(solution("camelCase"), "camel Case")
print(solution("breakCamelCase"), "break Camel Case")
