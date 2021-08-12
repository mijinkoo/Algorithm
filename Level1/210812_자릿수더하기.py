# 소스1
# map 이용해서 리스트 원소의 타입 변환
def solution(n):
    answer = []
    for i in str(n):
        answer.append(i)
    answer = list(map(int, answer))
    return sum(answer)

# 소스2
def sum_digit(number):
    return sum([int(i) for i in str(number)])

n = 123
print(solution(n))