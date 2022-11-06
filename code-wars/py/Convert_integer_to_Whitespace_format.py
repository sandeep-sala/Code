def whitespace_number(n):
    if n==0:
        return " \n"
    k,p = {"0":" ","1":"\t"},""
    p+= "\t" if n<0 else " "
    for i in f"{abs(n):b}":
        p+=k[i]
    return p+"\n"



print(whitespace_number( 1),    " \t\n")
print(whitespace_number( 0),      " \n")
print(whitespace_number(-1),   "\t\t\n")
print(whitespace_number( 2),   " \t \n")
print(whitespace_number(-3), "\t\t\t\n")