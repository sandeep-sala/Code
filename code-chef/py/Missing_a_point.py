
def check(A, B, C):
    c1_x = A[0]
    c1_y = A[1]

    c2_x = B[0]
    c2_y = B[1]

    c3_x = C[0]
    c3_y = C[1]

    c4_x = 0
    c4_y = 0

    if c1_x == c2_x or c1_x==c3_x:
        if c1_x == c2_x:
            c4_x=c3_x
        else:
            c4_x=c2_x
    else:
        c4_x=c1_x
    if c1_y == c2_y or c1_y==c3_y:
        if c1_y == c2_y:
            c4_y=c3_y
        else:
            c4_y=c2_y
    else:
        c4_y=c1_y

    return [c4_x, c4_y]



def IsRectangle( (x1, y1), (x2, y2), (x3, y3), (x4,y4) ):
    x2 -= x1
    x3 -= x1 
    x4 -= x1
    y2 -= y1
    y3 -= y1 
    y4 -= y1
    return (x2 + x3 == x4 and y2 + y3 == y4 and x2 * x3 == -y2 * y3) or(x2 + x4 == x3 and y2 + y4 == y3 and x2 * x4 == -y2 * y4) or (x3 + x4 == x2 and y3 + y4 == y2 and x3 * x4 == -y3 * y4)