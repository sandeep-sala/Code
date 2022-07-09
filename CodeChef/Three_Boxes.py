try:
    def get_no_of_bags(A,B,C,D):
        if( (A+B+C) <= D):
            return 1
        if((A+C) <= D) or ((A+B) <= D):
            return 2
        return 3

    for _ in range(int(input())):
        A,B,C,D = map(int,input().split())
        print(get_no_of_bags(A,B,C,D))
except:
    pass