def camel_case(string):
    return "".join(string.strip().title().split())

print(camel_case("test case"), "TestCase")
print(camel_case("camel case method"), "CamelCaseMethod")
print(camel_case("say hello "), "SayHello")
print(camel_case(" camel case word"), "CamelCaseWord")
print(camel_case(""), "")