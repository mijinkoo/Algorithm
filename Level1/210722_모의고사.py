def solution(answers):
    answer = [0,0,0]
    maxnum=[]
    num1= [1, 2, 3, 4, 5]
    num2= [2, 1, 2, 3, 2, 4, 2, 5]
    num3= [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i]== num1[i%len(num1)]:
            answer[0] +=1
        if answers[i] == num2[i%len(num2)]:
            answer[1] +=1
        if answers[i] == num3[i%len(num3)]:
            answer[2] +=1
    for i in range(len(answer)):
        if max(answer)==answer[i]:
            maxnum.append(i+1)
    return maxnum

# 파이썬에서 리스트 비교할 땐 enumerate 함수를 쓰자
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result