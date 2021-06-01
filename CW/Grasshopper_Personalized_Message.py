def greet(name, owner):
    return f"Hello guest" if owner != name else f"Hello boss"

print(greet('Daniel', 'Daniel'), 'Hello boss')
print(greet('Greg', 'Daniel'), 'Hello guest')

