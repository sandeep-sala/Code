def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    if n <= 10:
        respond = dogs[0]
    elif n <= 50:
        respond = dogs[1]
    elif n == 101:
        respond = dogs[3]
    else:
        respond = dogs[2]
    return respond

print(how_many_dalmatians(26), "More than a handful!")
print(how_many_dalmatians(8), "Hardly any")
print(how_many_dalmatians(14), "More than a handful!")
print(how_many_dalmatians(80), "Woah that's a lot of dogs!")
print(how_many_dalmatians(100), "Woah that's a lot of dogs!")
print(how_many_dalmatians(50), "More than a handful!")
print(how_many_dalmatians(10), "Hardly any")
print(how_many_dalmatians(101), "101 DALMATIONS!!!")