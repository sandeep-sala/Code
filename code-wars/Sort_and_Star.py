def two_sort(array):
    return "***".join( list(sorted(array)[0]) )


print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]), 'b***i***t***c***o***i***n' )
print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]), 'a***r***e')
print(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]), 'a***b***o***u***t')
print(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]), 'c***o***d***e')
print(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]), 'L***e***t***s')