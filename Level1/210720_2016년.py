#2016년은 윤년, 2월 29일이 말일
# 1월 1일이 금요일
def solution(a, b):
    month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day = {1:"FRI", 2:"SAT", 3:"SUN", 4:"MON", 5:"TUE", 6:"WED", 0:"THU"}
    sum = 0
    for i in range(a-1):
        sum += month[i+1]
    sum += b
    print(sum)
    answer = day[sum%7]
    return answer