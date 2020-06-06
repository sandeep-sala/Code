try:
    for _ in range(int(input())):
        n = str(input() ).lower()
        if n == 'b':
            print('BattleShip')
        if n == 'c':
            print('Cruiser')
        if n == 'd':
            print('Destroyer')
        if n == 'f':
            print('Frigate')
except:
    pass