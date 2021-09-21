# [kakao] 실패율
# 리스트 혹은 문자열에서 특정 원소의 개수를 찾는 함수 - list.count

# 소스1.
def solution(N, stages):
    fail_list = [0] * N
    
    for i in range(1, N + 1):
        challenge = len([x for x in stages if x >= i])
        fail = stages.count(i)
        if challenge == 0: 
            break
        fail_list[i - 1] = fail / challenge
    
    l = []
    for i, v in enumerate(fail_list):
        l.append((v, i + 1))
    sorted_l = sorted(l, key = lambda x : (x[0], -x[1]), reverse=True)
    return [i[1] for i in sorted_l]


# 소스2.
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]	
print(solution(N, stages))
print(solution(4,[4,4,4,4,4]))