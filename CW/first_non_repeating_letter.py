def first_non_repeating_letter(string):
    for i in string:
        if string.lower().count(i.lower()) == 1:
            return i
    return ''


print(first_non_repeating_letter('a'), 'a')
print(first_non_repeating_letter('stress'), 't')
print(first_non_repeating_letter('moonmen'), 'e')

print(first_non_repeating_letter(''), '')

print(first_non_repeating_letter('abba'), '')
print(first_non_repeating_letter('aa'), '')

print(first_non_repeating_letter('~><#~><'), '#')
print(first_non_repeating_letter('hello world, eh?'), 'w')

print(first_non_repeating_letter('sTreSS'), 'T')
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')