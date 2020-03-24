# Method 1

# def reverse_str(w):
#     t = ""
#     for i in w:
#         t = i+t
#     return t

# def is_Palindrome(s):
#     return str(s) == reverse_str(str(s))


# Method 2

def is_Palindrome(s):
    return str(s) == str(s)[::-1]

print(is_Palindrome("ABC"))
print(is_Palindrome("ABA"))
print(is_Palindrome(100))
print(is_Palindrome(101))