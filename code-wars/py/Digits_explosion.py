def explode(s):
    return "".join([ i*int(i) for i in s ])


sample_test_cases = [
    # (input, expected),
    ('312', '333122'),
    ('102269','12222666666999999999'),
    ('0', ''),
    ('000', ''),
    ('123', '122333'),
]

for s, expected in sample_test_cases:
    print(explode(s), expected)