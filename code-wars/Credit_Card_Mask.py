def maskify(cc):
    l = len(cc)
    return  cc if l < 4 else ("#"*(l-4)) + cc[-4:]

print(maskify(''), '')
print(maskify('123'), '123')
print(maskify('SF$SDfgsd2eA'), '########d2eA')