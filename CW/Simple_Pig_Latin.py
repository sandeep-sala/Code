def pig_it(text):
    return " ".join([ w[1:]+w[0]+'ay' if (len(w) > 1 and w.isalpha()  )else w for w in text.split(" ")  ])


print(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
print(pig_it('This is my string'),'hisTay siay ymay tringsay')