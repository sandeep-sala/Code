def solution(nums):
    return  sorted(nums) if nums else []

print(solution([1,2,3,10,5]), [1,2,3,5,10])
print(solution(None), [])
print(solution([]), [])
print(solution([20,2,10]), [2,10,20])
print(solution([2,20,10]), [2,10,20])