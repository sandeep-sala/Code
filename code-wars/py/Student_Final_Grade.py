def final_grade(exam, projects):
    if exam >= 90 or projects >= 10:
        return 100
    elif exam >= 75 and projects >= 5:
        return 90
    elif exam >= 50 and projects >= 2:
        return 75
    else:
        return 0



print(final_grade(100, 12), 100)
print(final_grade(85, 5), 90)