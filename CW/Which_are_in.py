def in_array(array1, array2):
    temp = set()
    for a1 in array1:
        if a1 not in temp:
            for a2 in array2:
                if a1 in a2:
                    temp.add(a1)
    return list(temp)




a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
print(in_array(a1,a2),r)
a1 = ["arp", "mice", "bull"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp']
print(in_array(a1,a2),r)
