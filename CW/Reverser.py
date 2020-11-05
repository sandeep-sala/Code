
def reverse(n ,s=0):
    if n:
        s = s*10 + n%10
        return reverse(n//10,s)   
    return s


print(reverse(1234), 4321)
print(reverse(10987), 78901)
print(reverse(1020), 201)