def sp_eng(sentence): 
    return True if "english" in sentence.lower() else False



print(sp_eng("english"), True)
print(sp_eng("egnlish"), False)
print(sp_eng("1234egn lis;h"), False);
print(sp_eng("1234english ;k"), True);
print(sp_eng("English"), True);
print(sp_eng("eNgliSh"), True);
print(sp_eng("1234#$%%eNglish ;k9"), True);
print(sp_eng("EGNlihs"), False);
print(sp_eng("1234englihs**"), False);
print(sp_eng(""), False)
