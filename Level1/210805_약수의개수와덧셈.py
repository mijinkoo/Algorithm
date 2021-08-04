def solution(left, right):
    count = [0 for _ in range(right - left + 1)]
    num = [x for x in range(left, right + 1)]
    for i in range(left, right + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                count[i-left] += 1
    
    answer = 0
    for i in range(len(count)):
        if count[i]%2==0:
            answer += num[i]
        else:
            answer -= num[i]
    return answer


# 약수의 개수가 홀수개라는 것은 제곱수라는 것과 필요충분
def solution2(left, right):
    answer = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer
