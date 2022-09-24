def sort_vowels(s):
    try:
        return "\n".join([ f"|{i}" if (i.lower() in {"a","e","i","o","u"}) else f"{i}|" for i in s ]) 
    except:
        return ''



print(sort_vowels('Codewars'), 'C|\n|o\nd|\n|e\nw|\n|a\nr|\ns|')
print(sort_vowels('Rnd Te5T'), 'R|\nn|\nd|\n |\nT|\n|e\n5|\nT|')
print(sort_vowels(1337), '')
print(sort_vowels(None), '')