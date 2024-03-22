def feast(beast, dish):
    return beast[0].lower() == dish[0].lower() and beast[-1].lower() == dish[-1].lower()


print(feast("great blue heron", "garlic naan"), True)
print(feast("chickadee", "chocolate cake"), True)
print(feast("brown bear", "bear claw"), False)
