def middle_me(N, X, Y): 
    return f"{Y*(N//2)}{X}{Y*(N//2)}" if N%2 == 0 else X

print(middle_me(18, 'z', '#'), '#########z#########')
print(middle_me(19, 'z', '#'), 'z')