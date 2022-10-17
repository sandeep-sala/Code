def is_isogram(s):
    s = s.lower()
    if s == "":
        return True
    for i in s:
        if s.count(i) > 1:
            return False
    return True


print(is_isogram("Dermatoglyphics"), True )
print(is_isogram("isogram"), True )
print(is_isogram("aba"), False, "same chars may not be adjacent" )
print(is_isogram("moOse"), False, "same chars may not be same case" )
print(is_isogram("isIsogram"), False )
print(is_isogram(""), True, "an empty string is a valid isogram" )