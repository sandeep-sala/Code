def expanded_form(num):
    return " + ".join([ ( j+"0"*( len(str(num)) - (i+1) ) ) for i,j in enumerate(str(num)) if j != '0' ])



print(expanded_form(12), '10 + 2')
print(expanded_form(42), '40 + 2')
print(expanded_form(70304), '70000 + 300 + 4')