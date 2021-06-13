def decode(string):
    return "".join([ {
        "1":"9",
        "2":"8",
        "3":"7",
        "4":"6",
        "5":"0",
        "6":"4",
        "7":"3",
        "8":"2",
        "9":"1",
        "0":"5"
    }[i] for i in string ])

print(decode("4103432323"), "6957678787")
print(decode("4103438970"), "6957672135")
print(decode("4104305768"), "6956750342")
print(decode("4102204351"), "6958856709")
print(decode("4107056043"), "6953504567")


