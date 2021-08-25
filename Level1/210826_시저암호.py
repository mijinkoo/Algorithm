# 알파벳 리스트 만드는 한줄 코드 -> import string

import string

def solution(s, n):
    low = [i for i in string.ascii_lowercase]
    up = [i for i in string.ascii_uppercase]
    s = list(s)
    for i in range(len(s)):
        if s[i] in low:
            s[i] = low[(low.index(s[i]) + n) % len(low)]
        elif s[i] in up:
            s[i] = up[(up.index(s[i]) + n) % len(up)]
    return ''.join(s)



print(solution(s = "AB", n = 1))
print(solution(s = "z", n = 1))
print(solution(s = "a B z", n = 4))

