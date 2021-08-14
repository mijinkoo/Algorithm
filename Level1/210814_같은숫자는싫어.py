# 소스1
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        else:
            if answer[len(answer)-1] == arr[i]:
                pass
            else:
                answer.append(arr[i])
    return answer
        
# 소스2
# 소스1에서 케이스를 여러 개로 나눈 것과 달리 슬라이싱을 이용함
# 빈 리스트에 대해 [:-1] 해도 오류가 발생하지 않음
def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]: 
            continue
        else:
            a.append(i)
    return a