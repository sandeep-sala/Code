# Method 1
def deleteDuplicate(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t


# Method 2
# def deleteDuplicate(s):
#     return list({i:i for i in s}.keys())

print(deleteDuplicate([1,2,3,3,4,5,9]))
print(deleteDuplicate([4,5,2,11,11,0]))
print(deleteDuplicate([1,2,3,4,5,6]))
print(deleteDuplicate([5,4,3,2,1]))