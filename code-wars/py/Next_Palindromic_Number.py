def is_palindromic(n):
    return n == n[::-1]

def next_pal(val):
    while True:
        val += 1
        if is_palindromic(str(val)):
            return val
    return -1



print(next_pal(11), 22)
print(next_pal(188), 191)
print(next_pal(191), 202)
print(next_pal(2541), 2552)