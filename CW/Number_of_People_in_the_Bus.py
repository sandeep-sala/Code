def number(bus_stops):
    sum = 0
    for (i,j) in bus_stops:
        sum += i
        sum -= j
    return sum


print(number([[10,0],[3,5],[5,8]]))  #,5)
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))  #,17)
print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))       #,21)