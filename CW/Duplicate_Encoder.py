def duplicate_encode(word):
    S = ""
    word = word.lower()
    for i in word:
        if word.count(i) > 1:
            S+=")"
        else:
            S+="("
    return S

# print(duplicate_encode("din"),"(((")
# print(duplicate_encode("recede"),"()()()")
# print(duplicate_encode("Success"),")())())","should ignore case")
print(duplicate_encode("U(JEN@JZMb"),'(()((()(((')