# 소스1.
def solution(x, n):
    xx = x
    answer = []
    for i in range(n):
        answer.append(x)
        x += xx
    return answer

# 소스2.
# 한줄로 구현하기
def solution2(x, n):
    return [i * x + x for i in range(n)]


print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))

