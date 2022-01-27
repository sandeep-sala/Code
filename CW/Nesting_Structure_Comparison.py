def same_structure_as(original,other, flag=True):
    if type(original) != type(other) and (type(original) == list or type(other) == list ):
        return False
    elif type(original) == list == type(other):
        if len(original) != len(other) :
            return False
        for i,j in zip(original, other):
            flag = same_structure_as(i,j)
    return flag


print(same_structure_as([[[],[]]],[[1,1]]))