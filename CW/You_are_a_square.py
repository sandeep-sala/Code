def is_square(n):
    if (n >= 0) and  str(n**(1/2)).split(".")[1] == '0' : return True
    return False 


print(is_square( -1))
print(is_square( 0))
print(is_square( 3))
print(is_square( 4))
print(is_square( 25))
print(is_square( 26))


