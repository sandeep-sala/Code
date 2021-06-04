def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i=0
    while (i < len(spl) ):
        if ( len(spl[i]) > longest):
            longest = len(spl[i])
        i+=1
    return longest


print(find_longest("The quick white fox jumped around the massive dog"), 7)
print(find_longest("Take me to tinseltown with you"), 10)
print(find_longest("Sausage chops"), 7)
print(find_longest("Wind your body and wiggle your belly"), 6)
print(find_longest("Lets all go on holiday"), 7)