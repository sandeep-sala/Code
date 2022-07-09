try:
    for __ in range(  int(input()) ):
        s = input()
        k, a = 0, []
        a = [ s[i:i+2] for i in range(0, len(s), 2) ]
        f = 0
        for i in a:
            if(i[0] == i[1]): 
                f = 1
                break     
        if(f == 0):
            print('yes')
        else:
            print('no')
except:
    pass