def bonus_time(salary, bonus):
    return f"${salary*10 if bonus else salary }"

bonus_time = lambda s,b: f"${s*10 if b else s }"

print(bonus_time(10000, True), '$100000')
print(bonus_time(25000, True), '$250000')
print(bonus_time(10000, False), '$10000')
print(bonus_time(60000, False), '$60000')
print(bonus_time(2, True), '$20')
print(bonus_time(78, False), '$78')
print(bonus_time(67890, True), '$678900')