def sum_str(a, b):
    return str(eval(f"{a or 0}+{b or 0}"))




print(sum_str("4","5"), "9")
print(sum_str("34","5"), "39")
print(sum_str("9",""), "9", "x + empty = x")
print(sum_str("","9"), "9", "empty + x = x")
print(sum_str("","") , "0", "empty + empty = 0")