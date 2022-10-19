def xo(s):
    s=s.lower()
    return  s.count("x")==s.count("o")

print(xo('xo'), 'True expected')
print(xo('xo0'), 'True expected')
print(not xo('xxxoo'), 'False expected')
