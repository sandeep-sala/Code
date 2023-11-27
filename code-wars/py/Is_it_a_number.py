def is_digit(s):
    try:
        float(s)
    except Exception:
        return False
    return True


print(is_digit("s2324"), False)
print(is_digit("-234.4"), True)
print(is_digit("3 4"), False)
print(is_digit("3-4"), False)
print(is_digit("3 4   "), False)
print(is_digit("34.65"), True)
print(is_digit("-0"), True)
print(is_digit("0.0"), True)
print(is_digit(""), False)
print(is_digit(" "), False)
