# 소스1.
def solution2(n):
    st = "수박"
    if n % 2 == 0:
        return st * (n // 2)
    else:
        return st * ((n - 1) // 2) + "수"

# 소스2.
# 슬라이싱을 이용한 간결한 코드
def solution(n):
    s = "수박" * n
    return s[:n]


print(solution(3))
print(solution(4))