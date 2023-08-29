class Menu:
    def __init__(self, p):
        self.i = 0
        p[self.i] = [p[self.i]]
        self.li = p
    
    def to_the_right(self):
        self.li[self.i] = self.li[self.i][0]
        self.i += 1
        if self.i >= len(self.li):
            self.i = 0
        self.li[self.i] = [self.li[self.i]]

    def to_the_left(self):
        self.li[self.i] = self.li[self.i][0]
        self.i -= 1
        if self.i < 0:
            self.i = len(self.li)-1
        self.li[self.i] = [self.li[self.i]]

    def display(self):
        return str(self.li)

menu = Menu(['1', '2', '3'])
menu2 = Menu(["a", "b", "c"])
print(menu.display(), "[['1'], '2', '3']")

menu.to_the_right()
print(menu.display(), "['1', ['2'], '3']")

menu.to_the_right()
print(menu.display(), "['1', '2', ['3']]")

menu.to_the_right()
print(menu.display(), "[['1'], '2', '3']")


print(menu2.display(), "[['a'], 'b', 'c']")

menu2.to_the_left()
print(menu2.display(), "['a', 'b', ['c']]")

menu2.to_the_left()
print(menu2.display(), "['a', ['b'], 'c']")

menu2.to_the_left()
print(menu2.display(), "[['a'], 'b', 'c']")
