with open("ttt.txt") as f:
    content = f.read()

# Count
print( len(content)  )

# Number
print( sum(map(str.isdigit, content)) )

# Upper
print( sum(map(str.isupper, content)) )

# lower
print( sum(map(str.islower, content)) )