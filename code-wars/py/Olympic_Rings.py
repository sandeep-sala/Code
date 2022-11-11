def olympic_ring(string):
    circle = {"a":1,"A":1,"b":1,"B":2,"d":1,"D":1,"e":1,"g":2,"o":1,"O":1,"p":1,"P":1,"Q":1,"R":1,"q":1,}
    s = 0
    for i in string:
        if i in circle:
            # s+=circle[i]
            s+=1
    s = s//2
    score = {1:"Not even a medal!",2:"Bronze!",3:"Silver!",4:"Gold!"}
    if s <= 1:
        return score[1]
    elif s == 2:
        return score[2]
    elif s == 3:
        return score[3]
    else:
        return score[4]


print(olympic_ring('QBVjKgcYD'), 'Bronze!')
# print(olympic_ring('eCEHWEPwwnvzMicyaRjk'), 'Bronze!')
# print(olympic_ring('JKniLfLW'), 'Not even a medal!')
# print(olympic_ring('EWlZlDFsEIBufsalqof'), 'Silver!')
# print(olympic_ring('IMBAWejlGRTDWetPS'), 'Gold!')