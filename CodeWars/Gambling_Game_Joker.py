
def joker_card(joker_nums, ticket_serials):
    prize_dict = {
        0: 'Losing card',
        1: 'Losing card',
        2: 'V type',
        3: 'IV type',
        4: 'III type',
        5: 'II type',
        6: 'I type'
    }
    prize = []
    joker = list(map( lambda x:str(x)[-1] ,joker_nums))[::-1]
    for tricket in ticket_serials:
        count = 0
        for i,num in enumerate(tricket[::-1]):
            if num == joker[i]:
                count += 1
            else:
                break
        prize.append(prize_dict[count])
    return prize



print(joker_card([12, 35, 1, 2, 23, 39], ['151239', '251229', '251339']), ["II type", "Losing card", "V type"])
print(joker_card([5, 45, 35, 25, 15, 1], ['555551', '235551', '555552']), ["I type", "III type", "Losing card"])
print(joker_card([2, 17, 33, 12, 39, 44], ['000022', '001194', '232294']), ["Losing card", "V type", "IV type"])
print(joker_card([20, 30, 40, 1, 2, 3], ['000123', '000125', '520123']), ["I type", "Losing card", "III type"])