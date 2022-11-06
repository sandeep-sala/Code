def lovefunc( flower1, flower2 ):
    is_even = lambda x : True if x % 2 == 0 else False
    return True if( is_even(flower1) == True and is_even(flower2) == False ) or ( is_even(flower1) == False and is_even(flower2) == True ) else False


print(lovefunc(1,4), True)
print(lovefunc(2,2), False)
print(lovefunc(0,1), True)
print(lovefunc(0,0), False)