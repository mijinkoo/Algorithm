'''def solution(n):
    num = {i for i in range(2, n + 1)}
    num2 = set()
    for i in num:
        for j in range(2, i):
            if i%j == 0:
                num2.add(i)
                break
    return len(num-num2)

print(solution(10))'''

# 소스1. 아래와 같은 코드를 제출했을 때 자꾸 시간초과...
#def solution(n):
#    num = [i for i in range(2, n + 1)]
#    for i in range(2, n + 1):
#        for j in range(2, i):
#            if i % j == 0:
#                num.remove(i)
#                break
#    return len(num)

# 소스2. 또 시간 초과... 2중 for문을 쓰면 안되나 봄...
'''def solution(n):
    num = n

    for i in range(2, n+1):
        for j in range(2, i):
            if i%j == 0:
                num -= 1
                break
    return num-1
print(solution(10))
print(solution(5))'''

# 소스3.
import math

def solution(n):
    num = {i for i in range(2, n+1)} # 2부터 n까지
    deci = {} # 소수  
    for i in range(n):
        if 