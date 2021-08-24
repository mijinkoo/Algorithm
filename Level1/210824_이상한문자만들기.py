# 문자열은 변경할 수 없음
# -> 리스트를 이용해서 바꾸거나, 
# -> + 연산을 이용해서 문자열을 추가할 수 있음
def solution(s):
    answer = s.split(" ")
    for i in range(len(answer)):
        st = ''
        for j in range(len(answer[i])):
            if j % 2 == 0:
                st += answer[i][j].upper()
            else:
                st += answer[i][j].lower()
        answer[i] = st
    return ' '.join(answer)


s = "try hello world"
print(solution(s))

