# 소스1.
# 리스트뿐만 아니라 문자열에 대해 coun() 함수 사용 가능
def solution(s):
    if (s.count('p') + s.count('P')) == (s.count('y') + s.count('Y')):
        return True
    else:
        return False

# 소스2.
# 모두 소문자로 바꾸고 개수를 세는 방법
def solution2(s):
    return s.lower().count('p')==s.lower().count('y')