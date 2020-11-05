def move_zeros(array):
    a , b = [] ,[]
    for i in array:
        if i == 0 and type(i) != bool:
            b.append(0)
        else:
            a.append(i)
    return a+b


# Test.describe("Basic tests")
print(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
print(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
print(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
print(move_zeros(["a","b"]),["a","b"])
print(move_zeros(["a"]),["a"])
print(move_zeros([0,0]),[0,0])
print(move_zeros([0]),[0])
print(move_zeros([False]),[False])
print(move_zeros([]),[])