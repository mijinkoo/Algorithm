def solution(d, budget):
    count = 0
    for i in sorted(d):
        if (budget - i) >= 0:
            budget -= i
            count += 1
        else:
            break
    return count

d = [1,3,2,5,4]
print(solution(d, budget=9))
d = [2,2,3,3]
print(solution(d, budget=10))