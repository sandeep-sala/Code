def update_light(current):
    return {"green":"yellow","yellow":"red","red":"green"}[current]


print(update_light('green'), 'yellow')
print(update_light('yellow'), 'red')
print(update_light('red'), 'green')