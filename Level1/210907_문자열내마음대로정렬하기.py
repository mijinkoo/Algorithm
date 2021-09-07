# sorted 함수에서 key lambda 사용해서 정렬 기준 여러 개 반영하기
def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n], x))



strings = ["abce", "abcd", "cdx"]
print(solution(strings, 2))
strings = ["sun", "bed", "car"]
print(solution(strings, 1))