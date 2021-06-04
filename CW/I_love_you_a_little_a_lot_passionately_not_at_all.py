def how_much_i_love_you(nb_petals):
    return {1:"I love you",2:"a little",3:"a lot",4:"passionately",5:"madly",0:"not at all"}[nb_petals%6]


how_much_i_love_you = lambda p: {
    0:"not at all",
    1:"I love you",
    2:"a little",
    3:"a lot",
    4:"passionately",
    5:"madly"}[p%6]


print(how_much_i_love_you(7),"I love you")
print(how_much_i_love_you(3),"a lot")
print(how_much_i_love_you(6),"not at all")


