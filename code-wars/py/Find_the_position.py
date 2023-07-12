import string
def position(alphabet):
    return f'Position of alphabet: {string.ascii_lowercase.index(alphabet)+1}'


tests = [
    # [input, expected]
    ["a", "Position of alphabet: 1"],
    ["z", "Position of alphabet: 26"],
    ["e", "Position of alphabet: 5"],
]

for inp, exp in tests:
    print(position(inp), exp)
