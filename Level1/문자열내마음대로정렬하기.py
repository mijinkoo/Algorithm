def solution(strings, n):
    
    return sorted(strings, key = lambda x: x[n])

strings = ["abce", "abcd", "cdx"]
print(solution(strings, 2))
strings = ["sun", "bed", "car"]
print(solution(strings, 1))