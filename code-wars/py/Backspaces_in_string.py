def clean_string(s):
    k = []
    for i in s:
        if i != "#":
            k.append(i)
        else:
            if k:
                k.pop()
    return "".join(k)


print(clean_string('abc#d##c'), "ac")
print(clean_string('abc####d##c#'), "" )
print(clean_string("#######"), "" )
print(clean_string(""), "" )