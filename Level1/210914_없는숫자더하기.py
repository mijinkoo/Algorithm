# 소스1.
def solution(numbers):
    num = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    sub = num - set(numbers)
    return sum(sub)

# 소스2.
def solution(numbers):
    num = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    sub = num - set(numbers)
    return sum(sub)
    
print(solution([1,2,3,4,6,7,8,0]))