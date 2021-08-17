# 소스1.
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer

# 소스2.
# Tip. 약수 관련 문제에서 num/2의 수들만 검사하면 아주 효율적임!
# -> 어차피 2를 약수로 가질 경우 최대 num/2를 약수로 갖기 때문에...
def solution(num):
    return num + sum([i for i in range(1, num // 2 + 1) if num % i == 0])

