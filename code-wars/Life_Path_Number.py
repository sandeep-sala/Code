def life_path_number(n):
    if "-" in n:
        d = 0
        for i in n.split("-"):
            d += int( life_path_number(i) )
        return int(life_path_number(str(d)))

    if len(n) == 1: 
        return n
    else: 
        return life_path_number(  str(sum(map(int,list(str(n))))) )
     

    

print(life_path_number("1955-10-28"), 4)    
print(life_path_number("1971-06-28"), 7)
