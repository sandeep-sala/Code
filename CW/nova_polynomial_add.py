def poly_add(p1, p2):
    if p1 == [] : return p2
    if p2 == [] : return p1
    return [p1[0] + p2[0]] + poly_add(p1[1:],p2[1:])





print(poly_add([1], [1]),  [2], "Two polynomial of order zero fail.")
print(poly_add([1,2], [1]),  [2,2], "Mixed length polynomials fail.")
print(poly_add([1,2,3,4], [4,3,2,1]), [5,5,5,5])
print(poly_add([],[]), [])
print(poly_add([1,2,3,4,5,6], []), [1,2,3,4,5,6])
print(poly_add([], [1,2,3,4,5,6]), [1,2,3,4,5,6])