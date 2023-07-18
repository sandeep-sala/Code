def greet(lg):
    ld = {
        'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }
    return ld[lg] if lg in ld else ld['english']


print(greet('english'), 'Welcome')
print(greet('dutch'), 'Welkom')
print(greet('IP_ADDRESS_INVALID'), 'Welcome')
print(greet(''), 'Welcome')
print(greet(2), 'Welcome')