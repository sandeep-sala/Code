"""
  The following implementation assumes that the activities 
    are already sorted according to their finish time
  Prints a maximum set of activities that can be done by a 
    single person, one at a time
"""

def printMaxActivities(s , f ): 
    n = len(f)
    i = 0
    l = [0,]
    for j in range(n): 
        if s[j] >= f[i]: 
            i = j
            l.append(j)
    return l

s = [1 , 3 , 0 , 5 , 8 , 5] 
f = [2 , 4 , 6 , 7 , 9 , 9] 
print( printMaxActivities(s , f) )
