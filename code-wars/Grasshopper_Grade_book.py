def get_grade(s1, s2, s3):
    avg = (s1+s2+s3)/3
    if 90 <= avg <= 100:
        return "A"
    elif 80 <= avg <= 90:
        return "B"
    elif 70 <= avg <= 80:
        return "C"
    elif 60 <= avg <= 70:
        return "D"
    else:
        return "F"

print(get_grade(95, 90, 93), "A", "get_grade(95, 90, 93)")
print(get_grade(100, 85, 96), "A", "get_grade(100, 85, 96)")
print(get_grade(92, 93, 94), "A", "get_grade(92, 93, 94)")
print(get_grade(100, 100, 100), "A", "get_grade(100, 100, 100)")
print(get_grade(70, 70, 100), "B", "get_grade(70, 70, 100)")
print(get_grade(82, 85, 87), "B", "get_grade(82, 85, 87)")
print(get_grade(84, 79, 85), "B", "get_grade(84, 79, 85)")
print(get_grade(70, 70, 70), "C", "get_grade(70, 70, 70)")
print(get_grade(75, 70, 79), "C", "get_grade(75, 70, 79)")
print(get_grade(60, 82, 76), "C", "get_grade(60, 82, 76)")
print(get_grade(65, 70, 59), "D", "get_grade(65, 70, 59)")
print(get_grade(66, 62, 68), "D", "get_grade(66, 62, 68)")
print(get_grade(58, 62, 70), "D", "get_grade(58, 62, 70)")
print(get_grade(44, 55, 52), "F", "get_grade(44, 55, 52)")
print(get_grade(48, 55, 52), "F", "get_grade(48, 55, 52)")
print(get_grade(58, 59, 60), "F", "get_grade(58, 59, 60)")
print(get_grade(0, 0, 0), "F", "get_grade(0, 0, 0)")