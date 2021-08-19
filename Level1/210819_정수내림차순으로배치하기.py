def solution(n):
    n = sorted(list(str(n)), reverse=True)
    return int(''.join(n))

n = 118372
print(solution(n))