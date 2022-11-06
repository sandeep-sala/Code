def problem(a):
    return "Error" if type(a) != int else (a*50)+6

problem = lambda a : "Error" if type(a) == str else (a*50)+6