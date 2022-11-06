def bouncing_ball(h, bounce, window):
    count = -1
    while h>window and 0<bounce<1 and 0<window<h:
        h = bounce * h
        count+=2
    return count


print(bouncing_ball(2, 0.5, 1), 1)
print(bouncing_ball(3, 0.66, 1.5), 3)
print(bouncing_ball(30, 0.66, 1.5), 15)
print(bouncing_ball(30, 0.75, 1.5), 21)
