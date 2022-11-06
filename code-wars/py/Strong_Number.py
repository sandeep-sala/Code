import math

def strong_num(n):
    return "STRONG!!!!" if n == sum([ math.factorial(int(i)) for i in str(n)]) else "Not Strong !!"


print(strong_num(1)  , "STRONG!!!!")
print(strong_num(2)  , "STRONG!!!!")
print(strong_num(145), "STRONG!!!!")

print(strong_num(7)  , "Not Strong !!")
print(strong_num(93) , "Not Strong !!")
print(strong_num(185), "Not Strong !!")
