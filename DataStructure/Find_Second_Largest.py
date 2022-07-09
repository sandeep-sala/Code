try: 
    a,b,c = int(input()),int(input()),int(input())
    find_second_largest = lambda a,b,c : sorted([a,b,c])[1]
    print(  find_second_largest(a,b,c)  )
except Exception as e:
    pass
    # print(e)
