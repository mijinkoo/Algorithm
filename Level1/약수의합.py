def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n%i == 0:
            answer += i
    return answer

# Tip. 소수 관련 문제에서 num/2의 수들만 검사하면 아주 효율적임!

# 소스2.
def solution(n):
    return n + sum([i for i in range()])

# https://programmers.co.kr/learn/courses/30/lessons/12928/solution_groups?language=python3