def wave(people):
    people = list(people)
    people_list = []
    for i,j in enumerate(people):
        if people[i].isalpha():
            temp = people.copy()
            temp[i] = temp[i].upper()
            people_list.append("".join(temp))
    return people_list


result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
print(wave("hello"), result)

result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
print(wave("codewars"), result)

result = []
print(wave(""), result)

result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
print(wave("two words"),result)

result = [" Gap ", " gAp ", " gaP "]
print(wave(" gap "), result)

result = ["A       b    ", "a       B    "]
print(wave("a       b    "), result)

result = ["This is a few words", "tHis is a few words", "thIs is a few words", "thiS is a few words", "this Is a few words", "this iS a few words", "this is A few words", "this is a Few words", "this is a fEw words", "this is a feW words", "this is a few Words", "this is a few wOrds", "this is a few woRds", "this is a few worDs", "this is a few wordS"]
print(wave("this is a few words"), result)
