# 소스1.
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        sum = []
        for j in range(len(arr1[0])):
            sum.append(arr1[i][j] + arr2[i][j])
        answer.append(sum)
    return answer

# 소스2.
# 소스1의 간결한 버전
def solution(arr1, arr2):
    for i in range(len(arr2)):
        for j in range(len(arr2[i])):
            arr1[i][j] += arr2[i][j]
    return arr1

# 소스3.
# zip, map 이용해서 for문 한 번만 사용하는 방법
def solution3(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        l = list(map(lambda x, y: x + y, i, j))
        answer.append(l)
    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution3(arr1, arr2))