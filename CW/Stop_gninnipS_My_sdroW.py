def spin_words(sentence):
    return " ".join([ i[::-1] if len(i) >= 5 else i for i in sentence.split()])

print(spin_words("Welcome"), "emocleW")
print(spin_words( "Hey fellow warriors" ), "Hey wollef sroirraw")
print(spin_words("This is a test"), "This is a test")
print(spin_words("his is another test"), "This is rehtona test")

