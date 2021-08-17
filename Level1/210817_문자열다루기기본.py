# 문자열이 숫자인지 확인하는 함수 isdigit()
# 문자열이 알파벳(문자)인지 확인하는 함수 isalpha()

# 소스1.
def solution(s):
    if len(s)==4 or len(s)==6:
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False

# 소스2
def solution2(s):
    return (len(s)==4 or len(s)==6) and s.isdigit()