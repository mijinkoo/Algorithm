# 소스1
def solution(n):
    answer = list(str(n))
    answer.reverse()
    return list(map(int, answer))

# 소스2
# reversed(string타입)
def digit_reverse(n):
    return list(map(int, reversed(str(n))))

n = 12345
print(solution(n))
