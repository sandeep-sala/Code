def number(lines):
    return [f"{i+1}: {j}" for i,j in enumerate(lines)]


print(number([]), [])
print(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])