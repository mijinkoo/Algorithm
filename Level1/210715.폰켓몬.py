def solution(nums):
    s = set(nums)
    if len(s)<=len(nums)/2:
        answer = len(s)
    else:
        answer = len(nums)/2
    return answer

# 간결한 풀이
def solution(nums):
    return min(len(nums)/2, len(set(nums)))
