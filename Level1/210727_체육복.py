def solution(n, lost, reserve):
    # case1. lost와 reserve의 교집합에 있는 학생의 경우
    res = list(set(reserve)-set(lost))
    for i in set(reserve).intersection(set(lost)):
        lost.remove(i)
    
    # case2.
    lost.sort()
    res.sort()
    res_minus = [r-1 for r in res]
    res_plus = [r+1 for r in res]
    for i in res_minus:
        for j in lost:
            if i==j:
                lost.remove(j)
                res_plus.remove(i+2)
    for i in res_plus:
        for j in lost:
            if i==j:
                lost.remove(j)  
    return n - len(lost)


############### 간결한 풀이 ###############
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)