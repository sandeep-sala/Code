def cakes(p, a):
    count = 0
    for i in p.keys():
        if i not in a:
            return count
    p = p.items()
    while True:
        ok = True
        for i in p:
            if a[i[0]] < i[1]:
                ok = False
        if ok:
            for i in p:
                a[i[0]] -= i[1]
            count += 1
        else:
            break
    return count



recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available), 2, 'example #1')

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe, available), 0, 'example #2')