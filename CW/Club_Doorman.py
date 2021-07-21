def pass_the_door_man(word):     
    for k, i in enumerate(word):
        if word[k] == word[k+1]:
            return (ord(i.lower()) - 96)*3



print( pass_the_door_man("lettuce") , 60)
print( pass_the_door_man("hill"), 36)
print( pass_the_door_man("apple"), 48)