def apple(x):
    return "It's hotter than the sun!!" if int(x)**2 > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."


print(apple('50'), "It's hotter than the sun!!")
print(apple(4), "Help yourself to a honeycomb Yorkie for the glovebox.")
print(apple("12"), "Help yourself to a honeycomb Yorkie for the glovebox.")
print(apple(60), "It's hotter than the sun!!")