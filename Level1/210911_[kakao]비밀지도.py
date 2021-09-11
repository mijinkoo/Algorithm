# 카카오 블라인드 [1차] 비밀지도

# 소스1. 
# bin() 함수를 쓰지 않은 비효율적인 코드 -> 내장함수들 기록하고 기억해두기!
def solution(n, arr1, arr2):
    map = []
    for x in range(len(arr1)):
        y = ""
        while arr1[x] > 0:
            y = str(arr1[x] % 2) + y
            arr1[x] //= 2
        arr1[x] = "0" * (n - len(y)) + y
    for x in range(len(arr2)):
        y = ""
        while arr2[x] > 0:
            y = str(arr2[x] % 2) + y
            arr2[x] //= 2
        arr2[x] = "0" * (n - len(y)) + y
    for i in range(len(arr1)):
        answer = ""
        num = int(arr1[i]) + int(arr2[i])
        num = "0" * (len(arr1) - len(str(num))) + str(num)
        for x in num:
            if int(x) >= 1:
                answer += "#"
            else:
                answer += " " 
        map.append(answer)
    return map

# 소스2.
# bin() 함수 10진수를 2진수로 만드는 함수
# rjust() 오른쪽 정렬 함수
# replace() 문자열에서 특정 문자열을 다른 문자열로 바꾸는 함수
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12 = a12.rjust(n,'0')
        a12 = a12.replace('1','#')
        a12 = a12.replace('0',' ')
        answer.append(a12)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))