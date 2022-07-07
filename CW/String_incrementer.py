import re

def incerment_number(n):
    return str(int(n)+1).zfill(len(n))

def increment_string(strng):
    s = re.split(r"([^0-9])",strng)
    if((s[-1]).isdigit()):
        return "".join(s[:-1]) + incerment_number(s[-1])
    return "".join(s) + "1"


print(increment_string("foo"), "foo1")
print(increment_string("foobar001"), "foobar002")
print(increment_string("foobar1"), "foobar2")
print(increment_string("foobar00"), "foobar01")
print(increment_string("foobar99"), "foobar100")
print(increment_string("foobar099"), "foobar100")
print(increment_string(""), "1")