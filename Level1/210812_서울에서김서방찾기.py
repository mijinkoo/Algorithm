# 소스1
# index 함수
def solution(seoul):
    return "김서방은 " + str(seoul.index("Kim")) + "에 있다"

# 소스2
# format{}
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))


seoul = ["Jane", "Kim"]
print(solution(seoul))
print(findKim(seoul))