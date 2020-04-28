def namelist(names):
    name_length = len(names)
    if name_length == 0:
        return ''
    elif name_length == 1:
        return names[0]['name']
    else:
        return '{} & {}'.format(", ".join(name["name"] for name in names[:-1] ),names[-1]["name"])

p = namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])   
p = namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
p = namelist([ {'name': 'Bart'} ])
# p = namelist([])
print(p)