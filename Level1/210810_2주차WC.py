# 2주차 위클리 챌린지
# 상호 평가

def solution(scores):
    answer = []
    for i in range(len(scores[0])):
        # 2차원 배열에서 열을 기준으로 값을 추출
        score = list(list(zip(*scores))[i])
 
        if scores[i][i]==min(score) or scores[i][i]==max(score):
            if score.count(scores[i][i])==1:
                score.remove(scores[i][i])
        mean = sum(score)/len(score)
        if mean >= 90:
            answer.append("A")
        elif 80 <= mean < 90:
            answer.append("B")
        elif 70 <= mean < 80:
            answer.append("C")
        elif 50 <= mean < 70:
            answer.append("D")
        elif mean < 50:
            answer.append("F")
    return ''.join(answer)
