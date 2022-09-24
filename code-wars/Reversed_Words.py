def reverse_words(s):
    return " ".join(s.split(" ")[::-1])

print(reverse_words("hello world!"), "world! hello")