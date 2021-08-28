# 소스1.
def solution2(x):
    num = list(map(int, list(str(x))))
    s = sum(num)
    if x % s == 0:
        return True
    else:
        return False

# 소스2. 간결한 버전
def solution(x):
    return x % sum([int(i) for i in str(x)]) == 0

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))