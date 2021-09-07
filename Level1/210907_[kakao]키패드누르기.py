# [카카오 인턴] 키패드 누르기

# 소스1. 내가 작성한 코드
# 좌표를 이용하지 않고도 거리 계산을 하는 방법 - 수식을 잘 이용함
def solution(numbers, hand):
    answer = ""
    left, right = 10, 12
    for x in numbers:
        if x == 0:
            x = 11
        elif x in [1, 4, 7]:
            left = x
            answer += "L"
        elif x in [3, 6, 9]:
            right = x
            answer += "R"
        else:
            ld = abs(x - left) // 3 + abs(x - left) % 3
            rd = abs(x - right) // 3 + abs(x - right) % 3
            if ld > rd:
                answer += "R"
                right = x
            elif ld == rd:
                if hand=="right":
                    answer += "R"
                    right = x
                else:
                    answer += "L"
                    left = x
            else:
                answer += "L"
                left = x
    return answer

# 소스2.
# 키패드의 위치를 좌표로 저장하는 방법
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer


numbers = [8, 4, 5, 9, 5]
hand = "right"
result = "LRLLLRLLRRL"
print(solution(numbers, hand))
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]