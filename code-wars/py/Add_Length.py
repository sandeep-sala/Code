def add_length(sent):
    return list(map(lambda x: f"{x} {len(x)}", sent.split(" ")))


print(add_length('apple ban'), ["apple 5", "ban 3"])
print(add_length('you will win'), ["you 3", "will 4", "win 3"])
print(add_length('you'), ["you 3"])
print(add_length('y'), ["y 1"])
