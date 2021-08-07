# 소스1. 풀긴 풀었는데 리스트를 너무 남발함...
# - sorted가 대소문자도 구별해서 정렬해주는 줄 몰랐음
def solution(s):
    s = list(s)
    lower = []
    upper = []
    for i in range(len(s)):
        if s[i].isupper():
            upper.append(s[i])
        else:
            lower.append(s[i])
    st = sorted(lower, reverse=True) + sorted(upper, reverse=True)
    answer = st[0]
    for i in range(1, len(st)):
        answer += st[i]
    return answer

# 소스2.
def solution2(s):
    s = sorted(s, reverse=True)
    answer = s[0]
    for i in range(1, len(s)):
        answer += s[i]
    return answer

# 소스3.
# 파이썬 join 함수 - 리스트의 요소들을 하나의 문자열로 합쳐주는 함수
def solution3(s):
    return ''.join(sorted(s, reverse=True))