def bingo(ticket, win):
    c = 0
    for i in ticket:
        for j in i[0]:
            if ord(j) == i[1]:
                c += 1
                break
    return "Winner!" if c >= win else "Loser!"


print(bingo([["ABC", 65], ["HGR", 74], ["BYHT", 74]], 2), "Loser!")
print(bingo([["ABC", 65], ["HGR", 74], ["BYHT", 74]], 1), "Winner!")
print(bingo([["HGTYRE", 74], ["BE", 66], ["JKTY", 74]], 3), "Loser!")
