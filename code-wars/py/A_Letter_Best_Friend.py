def best_friend(txt, a, b):
    for i in range(len(txt)):
        try:
            if txt[i] == a and txt[i+1] != b:
                return False
        except Exception:
            return False
    return True


print(best_friend('he headed to the store', 'h', 'e'), True)
print(best_friend('i found an ounce with my hound', 'o', 'u'), True)
print(best_friend('those were their thorns they said', 't', 'h'), True)
print(best_friend('we found your dynamite', 'd', 'y'), False)
print(best_friend('look they took the cookies', 'o', 'o'), False)
print(best_friend('a test', 't', 'e'), False)
print(best_friend('abcdee', 'e', 'e'), False)
print(best_friend('abcde', 'e', 'e'), False)
