def automorphic(n):
    p = str(n)
    return "Automorphic" if (str(n**2)[-len(p):]) == p  else "Not!!"


print(automorphic(1),"Automorphic")
print(automorphic(3),"Not!!")
print(automorphic(6),"Automorphic")
print(automorphic(9),"Not!!")
print(automorphic(25),"Automorphic")
print(automorphic(53),"Not!!")
print(automorphic(76),"Automorphic")
print(automorphic(95),"Not!!")
print(automorphic(625),"Automorphic")
print(automorphic(225),"Not!!")
