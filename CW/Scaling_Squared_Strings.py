def scale(strng, k, n):
    return "" if strng=="" else "\n".join(list(  map( lambda x: "\n".join(["".join([ i*k for i in x ])]*n) ,strng.split("\n") )  ))
    

a = "abcd\nefgh\nijkl\nmnop"
r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
print(scale(a, 2, 3), r)
print(scale("", 5, 5), "")
print(scale("Kj\nSH", 1, 2),"Kj\nKj\nSH\nSH")