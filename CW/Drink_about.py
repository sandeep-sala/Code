def people_with_age_drink(age):
    return "drink toddy" if age < 14 else "drink coke" if age < 18 else "drink beer" if age < 21 else "drink whisky"



print(people_with_age_drink(13), 'drink toddy', "Wrong result for 13")
print(people_with_age_drink(0), 'drink toddy', "Wrong result for 0")
print(people_with_age_drink(17), 'drink coke')
print(people_with_age_drink(15), 'drink coke')
print(people_with_age_drink(14), 'drink coke')
print(people_with_age_drink(20), 'drink beer')
print(people_with_age_drink(18), 'drink beer')
print(people_with_age_drink(22), 'drink whisky')
print(people_with_age_drink(21), 'drink whisky')