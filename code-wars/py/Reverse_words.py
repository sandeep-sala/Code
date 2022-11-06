def reverse_words(text):
    return " ".join([i[::-1] for i in text.split(" ")])


print(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
print(reverse_words('apple'), 'elppa')
print(reverse_words('a b c d'), 'a b c d')
print(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')