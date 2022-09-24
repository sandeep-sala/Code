def disarium_number(n):
    return "Disarium !!" if sum([ (int(j)**i) for i,j in enumerate(str(n),1) ]) == n   else "Not !!"


print(disarium_number(89)  , "Disarium !!")
print(disarium_number(518) , "Disarium !!")
print(disarium_number(1024), "Not !!")