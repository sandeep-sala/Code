def is_anagram(test, original):
    test, original = test.lower(), original.lower()
    for i in test:
        if len(test) != len(original):
            return False 
        if test.count(i) != original.count(i):
            return False
    return True


print(is_anagram("foefet", "toffee"), True)
print(is_anagram("Buckethead", "DeathCubeK"), True)
print(is_anagram("Twoo", "WooT"), True)
print(is_anagram("dumble", "bumble"), False)
print(is_anagram("ound", "round"), False)
print(is_anagram("apple", "pale"), False)