def DNA_strand(dna):
    map_dict = {"A":"T","T":"A","C":"G","G":"C"}
    word = ""
    for letter in dna:
        word += map_dict[letter]
    return word

print(DNA_strand("AAAA"))  #,"TTTT","String AAAA is")
print(DNA_strand("ATTGC"))  #,"TAACG","String ATTGC is")
print(DNA_strand("GTAT"))   #,"CATA","String GTAT is")