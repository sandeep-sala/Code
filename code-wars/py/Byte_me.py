from sys import getsizeof

def total_bytes(object):
    return getsizeof(object)

message = "Testing for '{}'"
print(total_bytes("hello"), 54, message.format("hello"))
print(total_bytes(123), 28, message.format(123))
print(total_bytes('[":)", 1]'), 58, message.format('[":)", 1]'))
print(total_bytes({'john': 19}), 232, message.format('{"john": 19}'))
print(total_bytes("¡◢龘"), 80)
print(total_bytes(999_999), 28)
print(total_bytes((1,2)), 56)
print(total_bytes("㋛"*12345), 24764)


        