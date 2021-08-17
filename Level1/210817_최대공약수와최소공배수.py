# 소스1.
from math import gcd

def solution2(n, m):
    return [gcd(n, m), n * m // gcd(n, m)]

# 소스2.
def solution(n, m):
    gcd = lambda a, b : b if not a % b else gcd(b, a % b)
    lcm = lambda a, b : a * b //gcd(a, b)
    return [gcd(n, m), lcm(n, m)]
    
print(solution(3, 12))
print(solution(2, 5))
print(solution(5, 5))