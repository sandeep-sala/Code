from collections import Counter
def most_frequent_item_count(c):
    if c:
        return max(Counter(c).values())
    return 0


print(most_frequent_item_count([3, -1, -1]), 2, "didn't work for [3, -1, -1]")
print(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]), 5, "didn't work for [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]")
print(most_frequent_item_count([]), 0, "didn't work for []")
print(most_frequent_item_count([9]), 1, "didn't work for [9]")