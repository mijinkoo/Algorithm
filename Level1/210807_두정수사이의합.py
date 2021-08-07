# 소스1
'''def solution(a, b):
    if a==b:
        return a
    else:
        x = a
        a = min(a, b)
        b = max(x, b)
        return sum([i for i in range(a, b+1)])'''

def solution(a, b):
    if a == b:
        return a
    elif a > b:
        a, b = b, a
    return sum(range(a, b+1))

print(solution(5, 3))
print(solution(3, 3))