def solution(number):
    return  0 if number < 0 else sum({i for i in range(number) if i % 3 == 0 or i % 5 == 0})

print(solution(10), 23)