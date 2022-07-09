def likes(names):
    l = len(names)
    if l == 0:
        return "no one likes this"
    if l == 1:
        return names[0]+" likes this"
    if l == 2:
        return names[0]+" and "+names[1]+" like this"
    if l == 3:
        return names[0]+", "+names[1] +" and "+names[2]+" like this"
    else:
        return names[0]+", "+names[1] +" and "+str(l-2)+" others like this"

"""
def likes(names):
    formats = {
            0: "no one likes this",
            1: "{} likes this",
            2: "{} and {} like this",
            3: "{}, {} and {} like this",
            4: "{}, {} and {others} others like this"
        }
    n = len(names)
    return formats[min(n,4)].format(*names, others=n-2)
"""


print(likes([]), 'no one likes this')
print(likes(['Peter']), 'Peter likes this')
print(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')