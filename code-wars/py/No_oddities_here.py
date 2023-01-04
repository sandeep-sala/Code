def no_odds(values):
    return [v for v in values if v % 2 == 0]


print(no_odds([0, 1]), [0], "Zero through one")
print(no_odds([0, 1, 2, 3]), [0, 2], "Zero through three")
print(no_odds([1, 3, 5, 7, 9]), [], "Odds through ten")
print(no_odds([0, 2, 4, 6, 8, 10]), [0, 2, 4, 6, 8, 10], "Evens through ten")
print(no_odds([-1, -3, -5, -7, -9]), [], "Negative odds")
print(no_odds([2, 4, 8, 6, 0]), [2, 4, 8, 6, 0], "Out of order")
print(no_odds([]), [], "Empty list")
