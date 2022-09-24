def multi_table(number):
    s = ''
    for i in range(1,11):
        s+= f'{i} * {number} = {i*number}'
        if i != 10:
            s+='\n'
    return s




print(multi_table(5))
print(multi_table(1))