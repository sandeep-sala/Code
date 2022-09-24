from requests import get as g
def countries_by_currency():
    c_code = {}
    r = g("https://restcountries.eu/rest/v2/").json()
    for i in r :
        for j in i["currencies"]:
            if j["code"] not in c_code:
                c_code[j["code"]]=[i["name"]]
            else:
                if i["name"] not in c_code[j["code"]]:
                    c_code[j["code"]].append(i["name"]) 
    return c_code


curr_dict = countries_by_currency()
result1 = curr_dict['NOK']
print(result1, ['Bouvet Island', 'Norway', 'Svalbard and Jan Mayen'])

result2 = curr_dict['CHF']
print(result2, ['Liechtenstein', 'Switzerland'])

result3 = curr_dict['PLN']
print(result3, ['Poland'])

