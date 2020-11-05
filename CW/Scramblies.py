# Not Done


def scramble(s1, s2):
    for i in s2:
        if s1.count(i) < s2.count(i): return False  
    return True


print(scramble('rkqodlw', 'world'),  True)
print(scramble('cedewaraaossoqqyt', 'codewars'), True)
print(scramble('katas', 'steak'), False)
print(scramble('scriptjava', 'javascript'), True)
print(scramble('scriptingjava', 'javascript'), True)
print(scramble('scriptjavx', 'javascript'), False)