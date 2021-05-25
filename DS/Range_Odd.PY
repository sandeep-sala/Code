try: 
    a,b = input().split()
    range_odd = lambda a,b : " ".join([ str(i) for i in range(int(a),int(b)+1) if i%2 != 0 ])
    print(  range_odd(a,b)  )
except Exception as e:
    pass
    # print(e)
