def game(words):
    for i in range(len(words)-1):
        if words[i] == "" : return []
        try:
            if words[i][-1] != words[i+1][0]:
                return words[:i+1]
        except:
            return words[:i+1]
    return words


# print(game(["dog","goose","elephant","tiger","rhino","orc","cat"]))
# print(game(['', '', '', '', '', '', '']))
print(game(['ab', 'bc', '', 'de', '', '', '']))
print(game(["","bc","","cd"]))
print(game(["ab","bc","","cd"]))
print(game(['apple', 'english', 'ham', 'mustard', 'daily', 'yum', 'machine', 'enchilada', 'apple', 'earth', 'honey', 'yourself', 'face', 'earbob', '']))


