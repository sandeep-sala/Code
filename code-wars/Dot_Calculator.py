def calculator(txt):
    l = txt.split(" ")
    l[0],l[-1] = l[0].count("."),l[-1].count(".")
    p = eval(f"{l[0]}{l[1]}{l[2]}")
    return "."*p or ""


print(calculator("..... + ...............") ,  "....................")
print(calculator("..... - ...") ,  "..")
print(calculator("..... - .") ,  "....")
print(calculator("..... * ...") ,  "...............")
print(calculator("..... * ..") ,  "..........")
print(calculator("..... // ..") ,  "..")
print(calculator("..... // ."), ".....")
print(calculator(". // .."), "")
print(calculator(". - ."), "")
