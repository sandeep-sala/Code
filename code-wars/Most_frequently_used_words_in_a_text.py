def top_3_words(text):
    t_l = text.split(" ")
    w_d = {}
    
    for i in t_l:
        if i=="":
            continue
        if any(map(str.isalpha, i)):
            if i.lower() in w_d:
                w_d[i.lower()] += 1
            else:
                w_d[i.lower()] = 1
    
    return  [ j[0] for j in sorted(w_d.items(), key=lambda x: x[1], reverse=True)][:3]


print(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
print(top_3_words("  //wont won't won't "), ["won't", "wont"])
print(top_3_words("  , e   .. "), ["e"])
print(top_3_words("  ...  "), [])
print(top_3_words("  '  "), [])
print(top_3_words("  '''  "), [])
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])