def disemvowel(string_):
    for i in 'AaEeIiOoUu':
        string_ = string_.replace(i,"")
    return string_

print(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")