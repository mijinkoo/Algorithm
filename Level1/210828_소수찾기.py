# 소스1.
from math import sqrt

def solution(n):
    cnt = 0
    for i in range(2, n + 1):
        prime = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            cnt += 1
    return cnt

# 소스2.
def solution(n):
    num = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)

print(solution(10))
print(solution(5))