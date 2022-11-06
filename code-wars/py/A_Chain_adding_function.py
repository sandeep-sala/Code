class add(int):
    def __call__(self, value):
        return add(self + value)


print(add(1), 1)
print(add(1)(2), 3)
print(add(1)(2)(3), 6)
