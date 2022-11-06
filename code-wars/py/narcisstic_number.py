def nar_rec(n ,l ,su=0):
    su += (n%10)**l
    if n < 10:
        return su
    return nar_rec(n//10 ,l ,su)

def narcissistic(n):
    if n == nar_rec(n ,len(str(n))):
        return True
    else:
        return False

print(narcissistic(122))
print(narcissistic(4887))