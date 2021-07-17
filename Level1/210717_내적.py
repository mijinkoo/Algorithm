def solution(a, b):
    answer = sum([x*y for x, y in zip(a, b)])
    return answer

def solution2(a, b):
    s = list(map(lambda i: a[i]*b[i], range(len(a))))
    return sum(s)