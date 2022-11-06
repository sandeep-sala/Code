def find_next_square(sq):
    p = str(sq ** 0.5).split(".")
    if p[-1] == '0':
        return (int(p[0])+1) ** 2
    return -1


print(find_next_square(121), 144, "Wrong output for 121")
print(find_next_square(625), 676, "Wrong output for 625")
print(find_next_square(319225), 320356, "Wrong output for 319225")
print(find_next_square(15241383936), 15241630849, "Wrong output for 15241383936")
print(find_next_square(155), -1, "Wrong output for 155")
print(find_next_square(342786627), -1, "Wrong output for 342786627")