def longest(a1, a2):
    return "".join(sorted(set(a1).union(set(a2))))

print(longest("aretheyhere", "yestheyarehere"), "aehrsty")
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
print(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
        