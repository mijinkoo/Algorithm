# 라이브러리를 사용해서 조합을 구현 + 소수 판별 알고리즘

from itertools import combinations

def solution(nums):
    com = list(combinations(nums, 3))
    count = 0
    for i in range(len(com)):
        b = 0
        for j in range(2, sum(com[i])//2):
            if sum(com[i]) % j == 0:
                b = 1
        if b == 0:
            count += 1
    return count

nums = [1, 2, 3, 4]
print(solution(nums))
nums = [1, 2, 7, 6, 4]
print(solution(nums))