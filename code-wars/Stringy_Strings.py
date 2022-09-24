def stringy(s):
    return "".join(["1" if j%2!=0 else "0" for j in range(1,s+1)])

print(stringy(3), '101', 'stringy(3)')
print(stringy(5), '10101', 'stringy(5)')
print(stringy(12), '101010101010', 'stringy(12)')
print(stringy(26), '10101010101010101010101010', 'stringy(26)')
print(stringy(28), '1010101010101010101010101010', 'stringy(28)')