def word_dic(w):
    d = {}
    for i in w:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d


def anagrams(word, words):
    dic = word_dic(word)
    return [ i for i in words if word_dic(i) == dic ]
    


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])