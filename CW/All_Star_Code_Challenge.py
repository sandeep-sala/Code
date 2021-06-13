def sum_ppg(playerOne, playerTwo):
    return playerOne["ppg"] + playerTwo["ppg"]


iverson = { 'team': '76ers', 'ppg': 11.2 }
jordan  = { 'team': 'bulls', 'ppg': 20.2 }
print(31.4, sum_ppg(iverson, jordan), 'Failed to sum iverson\'s and jordan\'s scores')
