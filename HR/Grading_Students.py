
def gradingStudents(grades):
    k=[]
    for g in grades:
        if g < 38:
            k.append(g)
            continue
        l = g
        while g%5 != 0:
            g += 1
        k.append( g if (g-l)<3 else l )
    return k

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    for i in result:
        print(i)