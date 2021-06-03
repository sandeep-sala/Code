def logical_calc(array, op):
    OP = {"AND":"&","OR":"|","XOR":"^"}
    val = array[0]
    for i in array[1:]:
        val = eval( f"{val} {OP[op]} {i}" )
    return val


print(logical_calc([True, False], "AND"), False)
print(logical_calc([True, False], "OR"), True)
print(logical_calc([True, False], "XOR"), True)
print(logical_calc([True, True, False], "AND"), False)
print(logical_calc([True, True, False], "OR"), True)
print(logical_calc([True, True, False], "XOR"), False)