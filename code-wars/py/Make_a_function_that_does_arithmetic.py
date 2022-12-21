def arithmetic(a, b, o):
    op_dict = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}
    return eval(f"{a}{op_dict[o]}{b}")


print(arithmetic(1, 2, "add"), 3, "'add' should return the two numbers added together!")
print(arithmetic(8, 2, "subtract"), 6, "'subtract' should return a minus b!")
print(arithmetic(5, 2, "multiply"), 10, "'multiply' should return a multiplied by b!")
print(arithmetic(8, 2, "divide"), 4, "'divide' should return a divided by b!")
