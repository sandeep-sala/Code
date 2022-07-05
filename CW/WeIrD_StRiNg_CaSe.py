def to_weird_case(n):
    return "".join([ i.upper() if not (j+1)%2==0 else i for j,i in enumerate(n)])



print(to_weird_case('String'), 'StRiNg')

print(to_weird_case('This is a test'), 'ThIs Is A TeSt')
