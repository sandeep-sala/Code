
def duplicate_count(text):
    d_count = 0
    text = text.lower()
    for i in set(text):
        if text.count(i) > 1:
            d_count += 1
    return d_count

print(duplicate_count(""), 0)
print(duplicate_count("abcde"), 0)
print(duplicate_count("Indivisibilities"), 2)
print(duplicate_count("abcdeaa"), 1)
print(duplicate_count("abcdeaB"), 2)
